# -*- coding: utf-8 -*-
# (c) Christian Meißner 2020

# pylint: disable=raise-missing-from
# pylint: disable=super-with-arguments

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import re
import json
import traceback
import inflection

from contextlib import contextmanager

try:
    import phpypam
    from phpypam import PHPyPAMEntityNotFoundException
    HAS_PHPIPAM = True
except ImportError:
    HAS_PHPIPAM = False
    PHPIPAM_IMP_ERR = traceback.format_exc()

from collections import defaultdict

from ansible.module_utils.basic import AnsibleModule, missing_required_lib

from ansible.utils.display import Display
display = Display()


class PhpipamAnsibleException(Exception):
    pass


class PhpipamAnsibleModule(AnsibleModule):
    """ Baseclass for all phpIPAM related ansible modules.
        Here we handle connection parameters.
    """

    _TOOLS_CONTROLLERS = (
        'tags',
        'devices',
        'device_types',
        'nameservers',
        'scanagents',
        'locations',
        'nat',
        'racks',
    )

    def __init__(self, **kwargs):
        # State recording for changed and diff reporting
        self._changed = False
        self._before = defaultdict(list)
        self._after = defaultdict(list)
        self._after_full = defaultdict(list)

        self.phpipam_spec, gen_args = self._phpipam_spec_helper(kwargs.pop('phpipam_spec', {}))
        argument_spec = dict(
            server_url=dict(required=True),
            app_id=dict(required=True),
            username=dict(required=True),
            password=dict(required=True, no_log=True),
        )
        argument_spec.update(gen_args)
        argument_spec.update(kwargs.pop('argument_spec', {}))
        supports_check_mode = kwargs.pop('supports_check_mode', True)

        super(PhpipamAnsibleModule, self).__init__(argument_spec=argument_spec, supports_check_mode=supports_check_mode, **kwargs)

        aliases = {alias for arg in argument_spec.values() for alias in arg.get('aliases', [])}
        self.phpipam_params = {k: v for (k, v) in self.params.items() if v is not None and k not in aliases}
        self.updated_entity = {}

        self.check_requirements()

        self._phpipamapi_server_url = self.phpipam_params.get('server_url')
        self._phpipamapi_app_id = self.phpipam_params.get('app_id')
        self._phpipamapi_username = self.phpipam_params.get('username')
        self._phpipamapi_password = self.phpipam_params.get('password')
        self._phpipamapi_ssl_verify = self.phpipam_params.get('ssl_verify', True)
        self._phpipamapi_path = kwargs.get('phpipam_path')
        self._phpipamapi_params = kwargs.get('phpipam_params')

        self.task_timeout = 60
        self.task_poll = 4

        self._thin_default = False
        self.state = 'undefined'

    @contextmanager
    def api_connection(self):
        """
        Context manager. Run a given code block after successful api connect.

        If the execution is done call `exit_json` to report the module has finished.
        """
        self.connect()
        yield
        self.exit_json()

    @property
    def changed(self):
        return self._changed

    def set_changed(self):
        self._changed = True

    def connect(self):
        self.phpipamapi = phpypam.api(
            url=self._phpipamapi_server_url,
            app_id=self._phpipamapi_app_id,
            username=self._phpipamapi_username,
            password=self._phpipamapi_password,
            ssl_verify=self._phpipamapi_ssl_verify,
            user_agent="phpipam-ansible-modules",
        )

    def find_entity(self, controller, path, params=None):
        try:
            result = self.phpipamapi.get_entity(controller=controller, controller_path=path, params=params)
        except PHPyPAMEntityNotFoundException:
            return None

        if type(result) == list:
            if len(result) == 1:
                result = result[0]
            else:
                if len(result) > 1:
                    error_msg = "too many ({0})".format(len(result))
                else:
                    error_msg = "no"
                self.fail_json(msg="Found {0} results while searching for {1} at {2}".format(error_msg, controller, path))

        return result

    def find_subnet(self, subnet, mask):
        # lookups for subnets need a separate find method
        # We only support cidr format to simplify the task.
        # CIDR is valid for ipv4 and ipv6 too.
        path = 'cidr/{0}/{1}'.format(subnet, mask)
        return self.find_entity('subnets', path)

    def find_address(self, address):
        path = 'search/{0}'.format(address)
        return self.find_entity('addresses', path)

    def find_vlan(self, vlan):
        return self.find_by_key(self.controller_uri, vlan)

    def find_by_key(self, controller, value, key='name'):
        """
        Some controllers don't provide the ability to search for entities by uri
        so we need the possibility to search via url parameters.
        this is done by parameters `filter_by` and `filter_value` in phpIPAM API

        :param controller: which controller to use
        :param value: the value for which we are looking for
        :param key: the key which we use for `filter_by`. Default is `name`.

        :return: An entity or `None` if no entity was found.
        """
        lookup_params = {
            'filter_by': key,
            'filter_value': value,
        }
        return self.find_entity(controller, '/', params=lookup_params)

    def set_entity(self, key):
        self.phpipam_spec[key]['resolved'] = True

    def _resolve_entity(self, key):
        if key not in self.phpipam_params:
            return None

        entity_spec = self.phpipam_spec[key]

        controller = entity_spec['controller'] or self.controller_uri

        if controller == 'subnets':
            subnet, mask = self.phpipam_params[key].split('/')
            result = self.find_subnet(subnet, mask)
        elif 'tools' in controller or controller in ['vlan', 'l2domains']:
            result = self.find_by_key(controller=controller, value=self.phpipam_params[key])
        else:
            if entity_spec.get('type') == 'entity':
                result = self.find_entity(controller=controller, path='/' + self.phpipam_params[key])
            elif entity_spec.get('type') == 'entity_list':
                flatten = entity_spec.get('flatten', False)
                if flatten:
                    flatten_result = [self.find_entity(controller=controller, path='/' + e)['id'] for e in self.phpipam_params[key]]
                    result = entity_spec.get('separator', ';').join(flatten_result)
            else:
                result = [self.find_entity(controller=controller, path='/' + value) for value in self.phpipam_params[key]]

        self.set_entity(key)

        return result

    def _auto_resolve_entities(self):
        """
        Here we resolve each parameter of type entity and create a updated_entity dict with
        all params and resolved params
        """

        desired_entity = {}
        for key, spec in self.phpipam_spec.items():
            """
            iterate over all params check wether it value has to be resolved.
            Create a new dictionary `updated_entity` with all key value pairs bare if they don't
            need to be resolved and the id of a resolved entity.
            On that way we also convert boolean into int as the api needed this type.
            """
            if key in self.phpipam_params:

                updated_key = spec.get('phpipam_name', key)

                if spec['type'] == 'entity' and 'resolved' not in spec:
                    desired_entity[updated_key] = self._resolve_entity(key)['id']
                elif spec['type'] == 'entity_list' and 'resolved' not in spec:
                    desired_entity[updated_key] = self._resolve_entity(key)
                else:
                    if spec['type'] == 'bool':
                        desired_entity[updated_key] = str(int(self.phpipam_params[key]))
                    else:
                        desired_entity[updated_key] = self.phpipam_params[key]

        return desired_entity

    def check_requirements(self):
        if not HAS_PHPIPAM:
            self.fail_json(msg=missing_required_lib("phpypam"), exception=PHPIPAM_IMP_ERR)

    def _phpipam_spec_helper(self, spec):
        """
        Create Ansible compatible argument_spec and
        prepare phpipam_spec for resolving each entitis.
        """
        phpipam_spec = {}
        argument_spec = {}

        _PHPIPAM_SPEC_KEYS = {
            'controller',
            'flatten',
            'phpipam_name',
            'phpipam_spec',
            'resolved',
            'separator',
        }
        _VALUE_SPEC_KEYS = {
            'controller',
            'flatten',
            'phpipam_name',
            'separator',
            'type',
        }

        for key, value in spec.items():
            phpipam_value = {k: v for (k, v) in value.items() if k in _VALUE_SPEC_KEYS}
            argument_value = {k: v for (k, v) in value.items() if k not in _PHPIPAM_SPEC_KEYS}

            phpipam_type = value.get('type')
            ansible_invisible = value.get('invisible', False)

            if 'phpipam_name' not in phpipam_value and '_' in key:
                phpipam_value['phpipam_name'] = inflection.camelize(key)

            if phpipam_type == 'entity':
                argument_value['type'] = 'str'
                if key == 'parent':
                    phpipam_value['controller'] = self.controller_uri
            elif phpipam_type == 'entity_list':
                argument_value['type'] = 'list'
                argument_value['elements'] = value.get('elements', 'str')
            elif phpipam_type:
                argument_value['type'] = phpipam_type

            phpipam_spec[key] = phpipam_value

            if not ansible_invisible:
                argument_spec[key] = argument_value

        return phpipam_spec, argument_spec

    def _create_entity(self, desired_entity):

        try:
            self.phpipamapi.create_entity(self.controller_uri, desired_entity)
            self.set_changed()
            if self.controller_name == 'subnet':
                entity = self.find_subnet(self.phpipam_params['subnet'], self.phpipam_params['mask'])
            elif self.controller_name == 'address':
                entity = self.find_address(self.phpipam_params['ipaddress'])
            elif 'tools' in self.controller_name or self.controller_name in ['vlan', 'l2domain']:
                entity = self.find_by_key(self.controller_uri, self.phpipam_params['name'])
            else:
                entity = self.find_entity(self.controller_uri, '/' + desired_entity['name'])
        except PHPyPAMEntityNotFoundException:
            entity = None

        return entity

    def _update_entity(self, desired_entity, current_entity):

        """
        There is a bug in l2domains controller. If we query a domain we get `sections`
        but if we want to set sections the controller expects `permissions`.
        This is not the best place to do it but we didn't expect a quick fix from phpIPAM developers.
        https://github.com/phpipam/phpipam/issues/3190
        """
        if self.controller_name == 'l2domain' and 'permissions' in desired_entity:
            current_entity['permissions'] = current_entity['sections']

        updated_entity = {k: v for k, v in desired_entity.items() if v != current_entity[k] and k != 'parent'}

        entity_id = 'id' in self.phpipam_spec and self.phpipam_spec['id']['phpipam_name'] or 'id'

        if updated_entity:
            if 'tools' not in self.controller_uri:
                updated_entity[entity_id] = current_entity[entity_id]
            if self.controller_uri == 'vlan':
                updated_entity['name'] = current_entity['name']
        else:
            return current_entity

        if 'tools' in self.controller_uri or self.controller_uri == 'vlan':
            update_path = current_entity[entity_id]
        else:
            update_path = '/'

        self.phpipamapi.update_entity(self.controller_uri, updated_entity, controller_path=update_path)

        try:
            if self.controller_name == 'subnet':
                entity = self.find_subnet(self.phpipam_params['subnet'], self.phpipam_params['mask'])
            elif self.controller_name == 'address':
                entity = self.find_address(self.phpipam_params['ipaddress'])
            elif 'tools' in self.controller_uri or self.controller_name in ['vlan', 'l2domain']:
                entity = self.find_by_key(self.controller_uri, self.phpipam_params['name'])
            else:
                entity = self.find_entity(self.controller_uri, '/' + current_entity['name'])
            self.set_changed()
        except PHPyPAMEntityNotFoundException:
            entity = None

        return entity

    def _delete_entity(self, current_entity):

        entity_id = 'id' in self.phpipam_spec and self.phpipam_spec['id']['phpipam_name'] or 'id'

        try:
            self.phpipamapi.delete_entity(self.controller_uri, current_entity[entity_id])
            self.set_changed()
        except PHPyPAMEntityNotFoundException:
            raise PhpipamAnsibleException("Entity '{0}' of type '{1}' can't be ensured absentd:\n{2}".format(current_entity['name'], self.controller_uri, traceback.format_exc()))

        return None

    def _controller(self, controller):
        if controller not in self.phpipamapi.controllers():
            raise PhpipamAnsibleException("The server doesn't know anything about controller '{0}'".format(controller))
        return True

    def exit_json(self, changed=False, **kwargs):
        kwargs['changed'] = changed or self.changed
        if 'diff' not in kwargs and (self._before or self._after):
            kwargs['diff'] = {'before': self._before,
                              'after': self._after}
        if 'entity' not in kwargs and self._after_full:
            kwargs['entity'] = self._after_full
        super(PhpipamAnsibleModule, self).exit_json(**kwargs)


class PhpipamEntityAnsibleModule(PhpipamAnsibleModule):

    def __init__(self, **kwargs):
        self.controller_name = kwargs.pop('controller_name', self.controller_name_from_class)
        self.controller_uri = self.controller_pluralize(self.controller_name)

        argument_spec = dict(
            state=dict(choices=['present', 'absent'], default='present'),
        )
        argument_spec.update(kwargs.pop('argument_spec', {}))
        super(PhpipamEntityAnsibleModule, self).__init__(argument_spec=argument_spec, **kwargs)

        self.state = self.params.pop('state')
        self.desired_absent = self.state == 'absent'
        self._thin_default = self.desired_absent

    @property
    def controller_name_from_class(self):
        """ Convert class name to controller name. The class name must follow folowing name convention:
            * Starts with Phpipam
            * Ends with Module

            This will convert PhpipamMyControllerModule class name to my/controller controller name.
            eg:
            * PhpipamSubnetModule => subnet
            * PhpipamSectionModule => section
            * ...
        """
        # Convert current class name from CamelCase to snake_case
        class_name = re.sub(r'(?<=[a-z])[A-Z]|[A-Z](?=[^A-Z])', r'_\g<0>', self.__class__.__name__).lower().strip('_')
        # Get controller name from snake case class name
        return '/'.join(class_name.split('_')[1:-1])

    def controller_pluralize(self, controller):
        """
        Most controller URIs exists in plural form but ansible modules use singular.
        So we create the plural for controllers here beside some few exceptions.
        For these exceptions we simply return the controller as it is.

        :param controller: The controller name which should be pluralized

        :return: The pluralized controller or the unchanged controller for exceptions
        """
        _PLURAL_EXCEPTIONS = (
            'nat',
            'prefix',
            'vlan',
        )

        if controller not in _PLURAL_EXCEPTIONS:
            controller = inflection.pluralize(controller)

        return controller

    def entity_name_to_id(self, entity_name):
        try:
            result = self.find_entity(controller=self.controller_uri, controller_path='/' + entity_name)
        except PHPyPAMEntityNotFoundException:
            raise PhpipamAnsibleException

        entity = json.load(result)

        try:
            return entity['id']
        except KeyError:
            raise PhpipamAnsibleException

    def record_before(self, controller, entity):
        self._before[controller].append(entity)

    def record_after(self, controller, entity):
        self._after[controller].append(entity)

    def reccord_after_full(self, controller, entity):
        self._after_full[controller].append(entity)

    def ensure_entity(self, desired_entity):

        state = self.state

        if self.controller_name == 'subnet':
            current_entity = self.find_subnet(self.phpipam_params['subnet'], self.phpipam_params['mask'])
        elif self.controller_name == 'address':
            current_entity = self.find_address(self.phpipam_params['ipaddress'])
        elif 'tools' in self.controller_name or self.controller_name in ['vlan', 'l2domain']:
            current_entity = self.find_by_key(self.controller_uri, self.phpipam_params['name'])
        else:
            current_entity = self.find_entity(self.controller_uri, '/' + self.phpipam_params['name'])

        updated_entity = None

        self.record_before(self.controller_uri, current_entity)

        if state == 'present':
            if current_entity is None:
                updated_entity = self._create_entity(desired_entity)
            else:
                updated_entity = self._update_entity(desired_entity, current_entity)
        elif state == 'absent':
            if current_entity is not None:
                updated_entity = self._delete_entity(current_entity)
        else:
            self.fail_json(msg="'{0}' is not a valid state.".format(state))

        self.record_after(self.controller_uri, updated_entity)

        return updated_entity

    def run(self, **kwargs):
        """
        Manage entities. Lookup, ensure, sanitize and manage parameters.
        """
        if ('parent' in self.phpipam_spec and self.phpipam_spec['parent'].get('type') == 'entity'
                and self.desired_absent and 'parent' in self.phpipam_params and self.loopup_entity('parent') is None):
            return None

        desired_entity = self._auto_resolve_entities()

        new_entity = self.ensure_entity(desired_entity)

        return new_entity
