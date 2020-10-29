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
module: device
version_added: 0.5.0
short_description: Manage devices
description:
    - create, update and delete devices
author:
    - "Christian Meißner (@cmeissner)"
options:
    hostname:
        description: Hostname of the given device
        type: str
        required: true
    ipaddress:
        description: IP address of the given device
        type: str
        required: false
    type:
        description:
            - Device type of this device.
            - The value have to reflect values from device types configured.
            - Default device types are I(Switch), I(Router), I(Firewall), I(Hub), I(Wireless), I(Database), I(Workstation), I(Laptop) and I(Other).
            - User defined types can be created eigther via UI, API (e.g. I(device_type) ansible module within this collection).
        type: str
        required: false
    description:
        description: A descriptive text for that entity
        type: str
        required: false
    sections:
        description: List of sections where the nameserver appears
        type: list
        required: false
    rack:
        description:
            - Rack where the device belongs to.
            - If set I(starting_rack_unit) and I(rack_units) are also required.
        type: str
        required: false
    starting_rack_unit:
        description:
            - Which is the starting rack unit where the device is mounted.
            - If set I(rack) and I(racK_units) are also required.
    rack_units:
        description:
            - Size of device in I(U).
            - If set I(rack) and I(starting_rack_unit) are also required.
        type: int
        required: false
    snmp_community:
        description: The SNMP community string
        type: str
        required: false
    snmp_version:
        description: The used SNMP version
        type: str
        required: false
    snmp_port:
        description: The used SNMP port
        type: str
        required: false
        default: 161
    snmp_timeout:
        description: The SNMP connection timeout
        type: str
        required: false
    snmp_queries:
        description:
        type: str
        required: false
    snmp_v3_sec_level:
        description: The used SNMPv3 security level
        type: str
        required: false
    snmp_v3_auth_protocol:
        description: The used SNMPv3 auth protocol
        type: str
        required: false
    snmp_v3_auth_pass:
        description: The password to authenticate via SNMPv3
        type: str
        required: false
    snmp_v3_priv_protocol:
        description: The used SNMPv3 privacy protocol
        type: str
        required: false
    snmp_v3_priv_pass:
        description: The password to authenticate via SNMPv3 in privacy mode
        type: str
        required: false
    snmp_v3_ctx_name:
        description: CTX name when using SNMPv3
        type: str
        required: false
    snmp_v3_ctx_engine_id:
        description: CTX engine id when using SNMPv3
        type: str
        required: false
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create device"
  codeaffen.phpipam.device:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    hostname: "leaf-example-01"
    ipaddress: "192.0.2.222"
    sections:
      - Example Inc.
      - DEVOPS department
    state: present

- name: "Remove device"
  codeaffen.phpipam.device:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "leaf-example-001"
    state: absent
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamDeviceModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamDeviceModule(
        phpipam_spec=dict(
            hostname=dict(type='str', required=True),
            ipaddress=dict(type='str', phpipam_name='ip'),
            type=dict(type='entity', controller='tools/device_types', default='Switch'),
            description=dict(type='str'),
            sections=dict(type='entity_list', controller='sections', flatten=True, separator=';'),
            rack=dict(type='entity', controller='racks'),
            starting_rack_unit=dict(type='int', phpipam_name='rack_start'),
            rack_units=dict(type='int', phpipam_name='rack_size'),
            snmp_community=dict(type='str', no_log=True, phpipam_name='snmp_community'),
            snmp_version=dict(type='str', phpipam_name='snmp_version'),
            snmp_port=dict(type='str', phpipam_name='snmp_port', default='161'),
            snmp_timeout=dict(type='str', phpipam_name='snmp_timeout'),
            snmp_queries=dict(type='str', phpipam_name='snmp_queries'),
            snmp_v3_sec_level=dict(type='str', phpipam_name='snmp_v3_sec_level'),
            snmp_v3_auth_protocol=dict(type='str', phpipam_name='snmp_v3_auth_protocol'),
            snmp_v3_auth_pass=dict(type='str', no_log=True, phpipam_name='snmp_v3_auth_pass'),
            snmp_v3_priv_protocol=dict(type='str', phpipam_name='snmp_v3_priv_protocol'),
            snmp_v3_priv_pass=dict(type='str', no_log=True, phpipam_name='snmp_v3_priv_pass'),
            snmp_v3_ctx_name=dict(type='str', phpipam_name='snmp_v3_ctx_name'),
            snmp_v3_ctx_engine_id=dict(type='str', phpipam_name='snmp_v3_ctx_engine_id'),
        ),
        required_together=['rack', 'starting_rack', 'rack_units'],
    )

    if not module.desired_absent:
        pass

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
