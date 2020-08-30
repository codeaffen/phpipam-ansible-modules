# -*- coding: utf-8 -*-
# (c) Christian Meißner 2020

# pylint: disable=raise-missing-from
# pylint: disable=super-with-arguments

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import traceback

try:
    from phpipam_client import PhpIpamClient, GET  # not yet needed, commented to prevent linting errors # , PATCH
    HAS_PHPIPAM = True
except ImportError:
    HAS_PHPIPAM = False
    PHPIPAM_IMP_ERR = traceback.format.exc()

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
        self._phpipamapi_path = self.kwargs.get('phpipam_path')
        self._phpipamapi_params = self.kwargs.get('phpipam_params')

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
