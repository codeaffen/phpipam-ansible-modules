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
module: vrf
version_added: 0.4.0
short_description: Manage virtual routers and forwarders
description:
    - create, update and delete L2 routing vrfs
author:
    - "Christian Meißner (@cmeissner)"
options:
    name:
        description: Name of the given vrf
        type: str
        required: true
    description:
        description: A descriptive text for that entity
        type: str
        required: false
    distinguisher:
        description: VRF route distinguisher
        type: str
        required: false
    sections:
        description: List of sections where the nameserver appears
        type: list
        required: false
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create vrf"
  codeaffen.phpipam.vrf:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my vrf"
    sections:
      - Example Inc.
      - DEVOPS department
    state: present

- name: "Remove vrf"
  codeaffen.phpipam.vrf:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my vrf"
    state: absent
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamVrfModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamVrfModule(
        phpipam_spec=dict(
            id=dict(type='int', invisible=True, phpipam_name='id'),
            name=dict(type='str', required=True),
            description=dict(type='str'),
            distinguisher=dict(type='str', phpipam_name='rd'),
            sections=dict(type='entity_list', controller='sections', flatten='true', separator=';'),
        )
    )

    if not module.desired_absent:
        pass

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
