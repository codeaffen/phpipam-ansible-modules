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
module: address
version_added: 0.2.0
short_description: Manage addresses
description:
    - create, update and delete sections
author:
    - "Christian Meißner (@cmeissner)"
options:
    subnet:
        description: subnet address belongs to
        type: str
        required: true
    ipaddress:
        description: IP address to hanle
        type: str
        required: true
        aliases:
            - ip
            - address
    is_gateway:
        description: Defines if address is presented as gateway
        type: bool
        required: false
        default: no
    description:
        description: Address description
        type: str
        required: false
    hostname:
        description: Address hostname
        type: str
        required: false
    mac_address:
        description: Mac address
        type: str
        required: false
        aliases:
            - mac
    owner:
        description: Address owner
        type: str
        required: false
    tag:
        description: IP tag (online, offline, ...)
        type: str
        required: false
    ignore_ptr:
        description: Controls if PTR should not be created
        type: bool
        required: false
        default: no
    ptr:
        description: DNS PTR record
        type: str
        required: false
    device:
        description: Device address belongs to
        type: str
        required: false
    port:
        description: Port
        type: str
        required: false
    note:
        description: Note
        type: str
        required: false
    exclude_ping:
        description: Exclude this address from status update scans
        type: bool
        required: false
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Reserve a IP address"
  codeaffen.phpipam.section:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    address: "192.0.2.1"
    description: "Default router of sunet"
    subnet: "192.0.2.0/24"
    is_gateway: yes
    state: present

- name: "Remove address reservation"
  codeaffen.phpipam.section:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    address: "192.0.2.1"
    subnet: "192.0.2.0/24"
    state: absent
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamAddressModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamAddressModule(
        phpipam_spec=dict(
            subnet=dict(type='entity', controller='subnets', required=True, phpipam_name='subnetId'),
            ipaddress=dict(type='str', required=True, aliases=['ip', 'address'], phpipam_name='ip'),
            is_gateway=dict(type='bool', phpipam_name='is_gateway'),
            description=dict(type='str'),
            hostname=dict(type='str'),
            mac_address=dict(type='str', aliases=['mac'], phpipam_name='mac'),
            owner=dict(type='str'),
            tag=dict(type='entity', controller='tags'),
            ignore_ptr=dict(type='bool'),
            ptr=dict(type='str'),
            device=dict(type='entity', controller='devices', phpipam_name='deviceId'),
            port=dict(type='str'),
            note=dict(type='str'),
            exclude_ping=dict(type='bool'),
        )
    )

    if not module.desired_absent:
        pass

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
