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
module: subnet
version_added: 0.0.1
short_description: Manage subnets
description:
    - create, update and delete subnets
author:
    - "Christian Meißner (@cmeissner)"
options:
    cidr:
        description:
            - Network in CIDR format.
            - Mutually exclusive with I(subnet) and I(mask).
        type: str
        required: false
        example:
            - 192.0.2.128/25
            - 2001:DB8::/32
    subnet:
        description:
            - Network address
            - Mutually exclusive with I(cidr).
            - If set, I(mask) is required.
        type: str
        required: false
        example:
            - 192.0.2.128
            - 2001:DB8::
    mask:
        description:
            - Subnet mask in octets for ipv4 subnets.
            - Prefix length (bits) for ipv6 subnets.
            - Mutually exclusive with I(cidr).
            - If set. I(subnet) is required.
    section:
        description: Name of the section under which the subnet is located
        type: int
        required: true
    description:
        description: Text which is shown in side bar if 'show as name' is selected
        type: str
        required: false
    master_subnet_cidr:
        description: CIDR of parent subnet
        type: str
        required: false
        example: 192.0.2.0/24
    show_as_name:
        description: If this is set to 'true' description is show in side bar instead of cidr
        type: bool
        required: false
        default: false
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create a subnet"
  codeaffen.phpipam.subnet:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    cidr: "192.0.2.128/26"
    section: "EXAMPLE INC"
    state: present

- name: "Create a subnet with parent"
  codeaffen.phpipam.subnet:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    cidr: "192.0.2.128/28"
    parent: "192.0.2.128/25"
    section: "DEVOPS department"
    state: present
'''

RETURN = '''
entity:
    description: Final state of the affected entities grouped by their type.
    returned: success
    type: dict
    contains:
        subnets:
            description: List of subnets.
            type: list
            elements: dicts
'''

import traceback
from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule, missing_required_lib
try:
    import ipaddress
    HAS_IPADDRESS = True
except ImportError:
    HAS_IPADDRESS = False
    IPADDRESS_IMP_ERR = traceback.format_exc()


class PhpipamSubnetModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamSubnetModule(
        argument_spec=dict(
            cidr=dict(type='str', required=False),
            subnet=dict(type='str', required=False),
            mask=dict(type='str', required=False),
            section=dict(type='str', required=True),
            description=dict(type='str', required=False),
            master_subnet_cidr=dict(type='str', required=False),
            show_as_name=dict(type='bool', required=False, default=False),
        ),
        mutually_exclusive=['cidr', 'subnet'],
        required_together=['subnet', 'mask'],
    )

    if not HAS_IPADDRESS:
        module.fail_json(msg=missing_required_lib("ipaddress"), exception=IPADDRESS_IMP_ERR)

    module_params = module.params

    if not module.desired_absent:
        if '/' not in module_params['cidr']:
            module.fail_json(msg='missing prefix lenght in "cidr". Need <ipaddr>/<prefix_lenght>.')
        else:
            if '.' in module_params['cidr'] and ':' not in module_params['cidr']:
                IPNetwork = ipaddress.IPv4Network
                module_params['mask'] = str(IPNetwork(u'%s' % (module_params['cidr'])).netmask)
            elif ':' in module_params['cidr'] and '.' not in module_params['cidr']:
                IPNetwork = ipaddress.IPv6Network
                module_params['mask'] = str(IPNetwork(u'%s' % (module_params['cidr'])).prefixlen)
            else:
                module.fail_json(msg='wrong formated "cidr". Need <ipaddr>/<prefix_lenght>.')
            module_params['subnet'] = str(IPNetwork(u'%s' % (module_params['cidr'])).network_address)
            del module_params['cidr']

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
