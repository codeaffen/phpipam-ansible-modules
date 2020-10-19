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


class PhpipamAnsibleException(Exception):
    pass


class PhpipamAnsibleModule(AnsibleModule):
    """ Baseclass for all phpIPAM related ansible modules.
        Here we handle connection parameters.
    """

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

    def find_subnet(self, cidr):
        # lookups for subnets need a separate find method
        # We only support cidr format to simplify the task.
        # CIDR is valid for ipv4 and ipv6 too.
        return self.find_entity(controller='subnet', controller_path='cidr/' + cidr)

    def find_tools(self, controller, value, key='name'):
        # tools controllers are special controllers that uses subcontrollers to work on specific objects.
        lookup_params = {
            'filter_by': key,
            'filter_value': value,
        }
        return self.find_entity(controller='tools/' + controller, params=lookup_params)

    def set_entity(self, key, entity):
        self.updated_entity[key] = entity
        self.phpipam_spec[key]['resolve'] = True

    def _resolve_entity(self, key):
        if key not in self.phpipam_params:
            return None

        entity_spec = self.phpipam_spec[key]

        controller = entity_spec['controller'] or self.controller_uri

        if controller == 'subnet':
            result = self.find_subnet(self.phpipam_params[key])
        if controller in ['nameserver', 'vlans', 'vrfs']:
            result = self.find_tools(controller=controller, value=self.phpipam_params[key])
        else:
            if entity_spec.get('type') == 'entity':
                result = self.find_entity(controller=controller, path='/' + self.phpipam_params[key])
            else:
                result = [self.find_entity(controller=controller, path='/' + value) for value in self.phpipam_params[key]]

        self.set_entity(key, result)

        return result

    def _auto_resolve_entities(self):
        """
        Here we resolve each parameter of type entity and create a updated_entity dict with
        all params and resolved params
        """

        for key, value in self.phpipam_params.items():
            """
            iterate over all params check wether it value has to be resolved.
            Create a new dictionary `updated_entity` with all key value pairs bare if they don't
            need to be resolved and the id of a resolved entity.
            On that way we also convert boolean into int as the api needed this type.
            """

            if key not in self.phpipam_spec:
                continue

            desired_entity = {}
            updated_key = self.phpipam_spec[key].get('phpipam_name', key)

            if self.phpipam_spec[key]['type'] == 'entity' and 'resolve' not in self.phpipam_spec[key]:
                desired_entity[updated_key] = self._resolve_entity(key)['id']
            else:
                if self.argument_spec[key]['type'] == 'bool':
                    desired_entity[updated_key] = int(self.phpipam_params[key])
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
            'phpipam_name',
            'phpipam_spec',
            'resolved',
        }
        _VALUE_SPEC_KEYS = {
            'type',
            'controller',
        }

        for key, value in spec.items():
            phpipam_value = {k: v for (k, v) in value.items() if k in _VALUE_SPEC_KEYS}
            argument_value = {k: v for (k, v) in value.items() if k not in _PHPIPAM_SPEC_KEYS}

            phpipam_type = value.get('type')
            ansible_invisible = value.get('invisible', False)
            phpipam_name = value.get('phpipam_name')

            if not phpipam_name and '_' in key:
                phpipam_name = inflection.camelize(key)

            if phpipam_type == 'entity':
                argument_value['type'] = 'str'
                if key == 'parent':
                    phpipam_value['controller'] = self.controller_uri
            elif phpipam_type:
                argument_value['type'] = phpipam_type

            if phpipam_name:
                phpipam_value['phpipam_name'] = phpipam_name
                phpipam_spec[phpipam_name] = {}
                if argument_value.get('type') is not None:
                    phpipam_spec[phpipam_name]['type'] = argument_value['type']

            phpipam_spec[key] = phpipam_value

            if not ansible_invisible:
                argument_spec[key] = argument_value

        return phpipam_spec, argument_spec

    def _create_entity(self, desired_entity):
        try:
            self.phpipamapi.create_entity(self.controller_uri, desired_entity)
            if self.controller_uri == 'subnet':
                entity = self.find_subnet(self.entity['name'])
            elif self.controller_uri in self._TOOLS_CONTROLLERS:
                entity = self.find_tools('tools/' + self.controller_uri, value=self.desired_entity['name'])
            else:
                entity = self.find_entity(self.controller_uri, '/' + desired_entity['name'])
        except PHPyPAMEntityNotFoundException:
            entity = None

        return entity

    def _update_entity(self, desired_entity, current_entity):
        updated_entity = {k: v for k, v in desired_entity.items() if v != current_entity[k] and k != 'parent'}
        if updated_entity:
            updated_entity['id'] = current_entity['id']
        else:
            return current_entity
        self.phpipamapi.update_entity(controller=self.controller_uri, controller_path='/', data=updated_entity)
        try:
            if self.controller_uri == 'subnet':
                entity = self.find_subnet(self.entity['name'])
            elif self.controller_uri in self._TOOLS_CONTROLLERS:
                entity = self.find_tools('tools/' + self.controller_uri, value=self.entity['name'])
            else:
                entity = self.find_entity(self.controller_uri, '/' + current_entity['name'])
        except PHPyPAMEntityNotFoundException:
            entity = None

        return entity

    def _delete_entity(self, current_entity):
        try:
            self.phpipamapi.delete_entity(self.controller_uri, current_entity['id'])
        except PHPyPAMEntityNotFoundException:
            raise PhpipamAnsibleException("Entity '{0}' of type '{1}' can't be ensured absentd:\n{2}".format(current_entity['name'], self.controller_uri, traceback.format_exc()))

        return None

    def _controller(self, controller):
        if controller not in self.phpipamapi.controllers():
            raise PhpipamAnsibleException("The server doesn't know anything about controller '{0}'".format(controller))
        return True

    def exit_json(self, changed=False, **kwargs):
        kwargs['changed'] = changed or self.changed
        super(PhpipamAnsibleModule, self).exit_json(**kwargs)


class PhpipamEntityAnsibleModule(PhpipamAnsibleModule):

    _TOOLS_CONTROLLERS = (
        'tag',
        'device',
        'device_type',
        'vlan',
        'vrf',
        'nameserver',
        'scanagent',
        'location',
        'nat',
        'rack',
    )

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

            This will convert PhpipamMyControllerModule class name to my_controller controller name.
            eg:
            * PhpipamSubnetModule => subnet
            * PhpipamSectionModule => section
            * ...
        """
        # Convert current class name from CamelCase to snake_case
        class_name = re.sub(r'(?<=[a-z])[A-Z]|[A-Z](?=[^A-Z])', r'_\g<0>', self.__class__.__name__).lower().strip('_')
        # Get controller name from snake case class name
        return '_'.join(class_name.split('_')[1:-1])

    def controller_pluralize(self, controller):
        _PLURAL_EXCEPTIONS = (
            'nat',
            'prefix',
        )

        if controller not in _PLURAL_EXCEPTIONS and controller not in self._TOOLS_CONTROLLERS:
            return inflection.pluralize(controller)
        elif controller in self._TOOLS_CONTROLLERS:
            if controller not in _PLURAL_EXCEPTIONS:
                return 'tools/' + inflection.pluralize(controller)
            else:
                return 'tools/' + controller
        else:
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

    def ensure_entity(self, desired_entity):

        state = self.state

        if self.controller_uri == 'subnet':
            current_entity = self.find_subnet(self.phpipam_params['cidr'])
        elif self.controller_uri in self._TOOLS_CONTROLLERS:
            current_entity = self.find_tools(controller=self.controller_uri, value=self.phpipam_params['name'])
        else:
            current_entity = self.find_entity(controller=self.controller_uri, path='/' + self.phpipam_params['name'])

        updated_entity = {}

        if state == 'present':
            pass
            if current_entity is None:
                pass  # create new entity
                updated_entity = self._create_entity(desired_entity)
            else:
                pass  # update existing entity
                updated_entity = self._update_entity(desired_entity, current_entity)
        if state == 'absent':
            if current_entity is not None:
                pass  # remove existing entity
                updated_entity = self._delete_entity(current_entity)

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
