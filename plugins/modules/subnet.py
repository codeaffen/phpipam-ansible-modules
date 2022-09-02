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
    subnet:
        description:
            - Network address
            - Mutually exclusive with I(cidr).
            - If set, I(mask) is required.
        type: str
        required: false
    mask:
        description:
            - Prefix length (bits) for ipv4 and ipv6 subnets.
            - Mutually exclusive with I(cidr).
            - If set. I(subnet) is required.
    description:
        description: Text which is shown in side bar if 'show as name' is selected
        type: str
        required: false
    section:
        description: Name of the section under which the subnet is located
        type: int
        required: true
    linked_subnet:
        description: Linked ipv6 subnet in CIDR format
        type: str
        required: false
    vlan:
        description: VLAN which the subnet should belongs to
        type: str
        required: false
    routing_domain:
        description:
            - Layer-2 routing domain the vlan belongs to
            - If you have I(vlan) with same number in different routing domains it need to be set on desired value
        type: str
        required: false
        default: default
    vrf:
        description: VRF which the sunet should belongs to
        type: str
        required: false
    parent:
        description: CIDR of parent subnet
        type: str
        required: false
        aliases:
            - master_subnet_cidr
    nameserver:
        description: Name of the DNS server which should attach to subnet
        type: str
        required: false
    show_as_name:
        description: If this is set to 'true' description is shown in side bar instead of CIDR
        type: bool
        required: false
        default: no
    permissions:
        description: JSON object that represent the permissions for each user
        type: json
        required: false
        default: None
    dns_recursive:
        description: Controls if PTR records should be created for subnet
        type: bool
        required: false
        default: no
    dns_records:
        description: Controls whether hostname DNS records are displayed
        type: bool
        required: false
        default: no
    allow_requests:
        description: Controls if IP requests are allowed for subnet
        type: bool
        required: false
        default: no
    scan_agent:
        description: Name of scanagent which should be used for subnet
        type: string
        required: false
    ping_subnet:
        description: Controls if subnet should be included in status checks
        type: bool
        required: false
        default: no
    discover_subnet:
        description: Controls if new hosts should be discovered for new host scans
        type: bool
        required: false
        default: no
    is_folder:
        description:
            - Controls if we are adding subnet or folder
            - can't be changed after subnet was created
        type: bool
        required: false
        default: no
    is_full:
        description: Marks subnet as used
        type: bool
        required: false
        default: no
    subnet_state:
        description: Assigned tag of the subnet.
        type: string
        required: false
    threshold:
        description: Subnet threshold
        type: int
        required: false
    location:
        description: Subnet location
        type: str
        required: false
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
            elements: dict
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
        phpipam_spec=dict(
            cidr=dict(type='str'),
            subnet=dict(type='str'),
            mask=dict(type='str'),
            description=dict(type='str'),
            section=dict(type='entity', required=True, controller='sections', phpipam_name='sectionId'),
            linked_subnet=dict(type='entity', phpipam_name='linked_subnet'),
            vlan=dict(type='entity', controller='vlan', phpipam_name='vlanId'),
            routing_domain=dict(type='str', api_invisible=True, default='default'),
            vrf=dict(type='entity', controller='vrf', phpipam_name='vrfId'),
            parent=dict(type='entity', phpipam_name='masterSubnetId'),
            nameserver=dict(type='entity', controller='tools/nameservers', phpipam_name='nameserverId'),
            show_as_name=dict(type='bool', phpipam_name='showName'),
            permissions=dict(type='json'),
            dns_recursive=dict(type='bool', phpipam_name='DNSrecursive'),
            dns_records=dict(type='bool', phpipam_name='DNSrecords'),
            allow_requests=dict(type='bool'),
            scan_agent=dict(type='entity', controller='tools/scanagents'),
            ping_subnet=dict(type='bool'),
            discover_subnet=dict(type='bool'),
            is_folder=dict(type='bool'),
            is_full=dict(type='bool'),
            subnet_state=dict(type='entity', phpipam_name='state'),
            threshold=dict(type='int'),
            location=dict(type='entity', controller='tools/locations'),
        ),
        mutually_exclusive=['cidr', 'subnet'],
        required_together=[['subnet', 'mask']],
    )

    if not HAS_IPADDRESS:
        module.fail_json(msg=missing_required_lib("ipaddress"), exception=IPADDRESS_IMP_ERR)

    module_params = module.phpipam_params

    if 'cidr' in module_params:
        if '/' not in module_params['cidr']:
            module.fail_json(msg='missing prefix lenght in "cidr". Need <ipaddr>/<prefix_lenght>.')
        else:
            IPNetwork = None
            if '.' in module_params['cidr'] and ':' not in module_params['cidr']:
                IPNetwork = ipaddress.IPv4Network
                module_params['mask'] = str(IPNetwork(u'%s' % (module_params['cidr'])).prefixlen)
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
