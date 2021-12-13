#!/usr/bin/env python

# -*- coding: utf-8 -*-
# (c) Christian Meißner 2020
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
---
module: device_type
version_added: 0.5.0
short_description: Manage device types
description:
    - create, update and delete device types
author:
    - "Christian Meißner (@cmeissner)"
options:
    name:
        description: Name of the given device type
        type: str
        required: true
    description:
        description: A descriptive text for that entity
        type: str
        required: false
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create device type"
  codeaffen.phpipam.device_type:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "USP"
    description: "universal power supply"
    description:
    state: present

- name: "Remove device type"
  codeaffen.phpipam.device_type:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "USP"
    state: absent
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamToolsDeviceTypeModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamToolsDeviceTypeModule(
        phpipam_spec=dict(
            id=dict(type='int', invisible=True, phpipam_name='tid'),
            name=dict(type='str', required=True, phpipam_name='tname'),
            description=dict(type='str', phpipam_name='tdescription'),
        )
    )

    if not module.desired_absent:
        pass

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
