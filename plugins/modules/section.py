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
module: section
version_added: 0.0.1
short_description: Manage sections
description:
    - create, update and delete sections
author:
    - "Christian Meißner (@cmeissner)"
options:
    name:
        description: Name of the section
        type: str
        required: true
    description:
        description: Short describtive text
        type: str
        required: false
        default: None
    parent:
        description: Name of the parent section
        type: str
        required: false
        default: None
        aliases:
            - master
            - master_section
    permissions:
        description: JSON object that represent the permissions for each user
        type: json
        required: false
        default: None
    strict_mode:
        description: If set to true, consistency of subnets and IP addresses will be checked
        type: bool
        required: false
        default: no
    subnet_ordering:
        description: How to order subnets within this section
        type: str
        required: false
        default: "subnet,asc"
    list_order:
        description: Order in sections list view
        type: int
        required: false
    show_vlan:
        description: Show/hide VLANs in subnet list view
        type: bool
        required: false
        default: no
    show_vrf:
        description: Show/hide VRFs in subnet list view
        type: bool
        required: false
        default: no
    show_supernets_only:
        description: Show only supernets in sebnet list view
        type: bool
        required: false
        default: no
    dns_resolver:
        description: The NS resolver to be used for this section
        type: str
        required: false
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create a section"
  codeaffen.phpipam.section:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "EXAMPLE INC"
    description: "Section for company EXAMPLE INC"
    state: present

- name: "Create a section with parent"
  codeaffen.phpipam.section:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "DEVOPS department"
    parent: "EXAMPLE INC"
    description: "Section for devops department in EXAMPLE INC"
    state: present
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamSectionModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamSectionModule(
        phpipam_spec=dict(
            name=dict(type='str', required=True),
            description=dict(type='str', required=False),
            parent=dict(type='entity', controller='sections', required=False, defautl=None, phpipam_name='masterSection'),
            permissions=dict(type='json', required=False, default=None),
            strict_mode=dict(type='bool', required=False),
            subnet_ordering=dict(type='bool', required=False, phpipam_name='subnetOrdering'),
            list_order=dict(type='bool', required=False, phpipam_name='order'),
            show_vlan=dict(type='bool', required=False, phpipam_name='showVLAN'),
            show_vrf=dict(type='bool', required=False, phpipam_name='showVRF'),
            show_supernets_only=dict(type='bool', required=False),
            dns_resolver=dict(type='entity', controller='tools/nameservers', required=False, phpipam_name='DNS'),
        )
    )

    if not module.desired_absent:
        pass

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
