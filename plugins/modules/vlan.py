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
module: vlan
version_added: 0.3.0
short_description: Manage vlans
description:
    - create, update and delete vlans
author:
    - "Christian Meißner (@cmeissner)"
options:
    name:
        description: Name of the given vlan
        type: str
        required: true
    description:
        description: A descriptive text for that entity
        type: str
        required: false
    vlan_id:
        description:
            - The VLAN-ID. Must be a number.
            - Due to implementation of api the value has to be I(string) here but is I(int) in phpIPAM
        type: str
        required: true
    routing_domain:
        description: Name of the L2 routing domain of that VLAN
        type: string
        required: false
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create vlan"
  codeaffen.phpipam.vlan:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my vlan"
    vlan_id: 1337
    state: present

- name: "Remove vlan"
  codeaffen.phpipam.vlan:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my vlan"
    state: absent
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamVlanModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamVlanModule(
        phpipam_spec=dict(
            id=dict(type='int', invisible=True, phpipam_name='vlanId'),
            name=dict(type='str', required=True),
            description=dict(type='str'),
            vlan_id=dict(type='str', required=True, phpipam_name='number'),
            routing_domain=dict(type='entity', controller='l2domains', phpipam_name='domainId', default='default')
        )
    )

    if not module.desired_absent:
        pass

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
