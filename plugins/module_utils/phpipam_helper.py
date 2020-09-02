# -*- coding: utf-8 -*-
# (c) Christian Meißner 2020

# pylint: disable=raise-missing-from
# pylint: disable=super-with-arguments

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import traceback

from contextlib import contextmanager

try:
    from phpipam_client import PhpIpamClient, GET  # not yet needed, commented to prevent linting errors # , PATCH
    HAS_PHPIPAM = True
except ImportError:
    HAS_PHPIPAM = False
    PHPIPAM_IMP_ERR = traceback.format_exc()

from collections import defaultdict

from ansible.module_utils.basic import AnsibleModule, missing_required_lib


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

        argument_spec = dict(
            state=dict(choices=['present', 'absent'], default='present'),
            server_url=dict(required=True),
            app_id=dict(required=True),
            username=dict(required=True),
            password=dict(required=True, no_log=True),
        )
        argument_spec.update(kwargs.pop('argument_spec', {}))
        supports_check_mode = kwargs.pop('supports_check_mode', True)

        super(PhpipamAnsibleModule, self).__init__(argument_spec=argument_spec, supports_check_mode=supports_check_mode, **kwargs)

        aliases = {alias for arg in argument_spec.values() for alias in arg.get('aliases', [])}
        self.phpipam_params = {k: v for (k, v) in self.params.items() if v is not None and k not in aliases}

        self.check_requirements()

        self._phpipamapi_server_url = self.phpipam_params.get('server_url')
        self._phpipamapi_app_id = self.phpipam_params.get('app_id')
        self._phpipamapi_username = self.phpipam_params.get('username')
        self._phpipamapi_password = self.phpipam_params.get('password')
        self._phpipamapi_path = kwargs.get('phpipam_path')
        self._phpipamapi_params = kwargs.get('phpipam_params')

        self.task_timeout = 60
        self.task_poll = 4

        self._thin_default = False
        self.state = 'undefined'

    @contextmanager
    def api_connection(self):
        self.connect()
        yield
        self.exit_json()

    @property
    def changed(self):
        return self._changed

    def connect(self):
        self.phpipamapi = PhpIpamClient(
            url=self._phpipamapi_server_url,
            app_id=self._phpipamapi_app_id,
            username=self._phpipamapi_username,
            password=self._phpipamapi_password,
            user_agent="phpipam-ansible-modules",
        )

    def sections(self):
        return self.phpipamapi.query('/sections/', method=GET)

    def get(self, path, params):
        return self.phpipamapi.get(path, params)

    def check_requirements(self):
        if not HAS_PHPIPAM:
            self.fail_json(msg=missing_required_lib("phpipam-client"), exception=PHPIPAM_IMP_ERR)

    def _create_entity(self):
        pass

    def _update_entity(self):
        pass

    def _delete_entity(self):
        pass

    def exit_json(self, changed=False, **kwargs):
        kwargs['changed'] = changed or self.changed
        super(ForemanAnsibleModule, self).exit_json(**kwargs)

class PhpipamEntityAnsibleModule(ForemanAnsibleModule):

    def __init__(self, **kwargs):
        self.entity_name = kwargs.pop('entity_name', self.entity_name_from_class)

        argument_spec = dict(
            state=dict(choices=['present', 'absent'], default='present'),
        )
        argument_spec.update(kwargs.pop('argument_spec', {}))
        super(PhpipamEntitiyAnsibleModule, self).__init__(argument_spec=argument_spec, **kwargs)

    @property
    def entity_name_from_class(self):
        """ Convert class name to entity name. The class name must follow folowing name convention:
            * Starts with Phpipam
            * Ends with Module

            This will concert PhpipamMyEntityModule class name to my_entity entity name.
            eg:
            * PhpipamSubnetModule => subnet
            * PhpipamSectionModule => section
            * ...
        """
        # Convert current class name from CamelCase to snake_case
        class_name = re.sub(r'(?<=[a-z])[A-Z]|[A-Z](?=[^A-Z])', r'_\g<0>', self.__class__.__name__).lower().strip('_')
        # Get entity name from snake case class name
        return '_'.join(class_name.split('_')[1:-1])
