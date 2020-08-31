# -*- coding: utf-8 -*-
# (c) Christian Meißner 2020

# pylint: disable=raise-missing-from
# pylint: disable=super-with-arguments

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import hashlib
import json
import os
import re
import time
import traceback
import yaml

from phpipam_client import PhpIpamClient, GET, PATCH

from contextlib import contextmanager

from collections import defaultdict
from functools import wraps

from ansible.module_utils.basic import AnsibleModule, missing_required_lib
from ansible.module_utils._text import to_bytes, to_native
from ansible.module_utils import six

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

        self._phpipamapi_server_url     = kwargs.get('server_url', 'http://localhost:8080/api')
        self._phpipamapi_app_id         = kwargs.get('app_id', 'ansible')
        self._phpipamapi_username       = kwargs.get('username', 'test')
        self._phpipamapi_password       = kwargs.get('password', 'test1234')

    def connect(self):
        self.phpipamapi = PhpIpamClient(
            url = self._phpipamapi_server_url,
            app_id = self._phpipamapi_app_id,
            username = self._phpipamapi_username,
            password = self._phpipamapi_password,
            user_agent = "phpipam-ansible-modules",
        )

    def sections(self):
        return self.phpipamapi.query('/sections/', method=GET)
