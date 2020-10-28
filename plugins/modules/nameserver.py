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
module: nameserver
version_added: 0.3.0
short_description: Manage nameservers
description:
    - create, update and delete nameservers
author:
    - "Christian Meißner (@cmeissner)"
options:
    name:
        description: Name of the given nameserver
        type: str
        required: true
    description:
        description: A descriptive text for that entity
        type: str
        required: false
    addresses:
        description: List of IP addresses the namerserver can be reached on
        type: list
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
- name: "Create nameserver"
  codeaffen.phpipam.nameserver:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "cloudflare dns"
    addresses:
      - 1.1.1.1
      - 1.0.0.1
    permissions: 1;2
    state: present

- name: "Remove nameserver
  codeaffen.phpipam.nameserver:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "cloudflare dns"
    state: absent
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamToolsNameserverModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamToolsNameserverModule(
        phpipam_spec=dict(
            name=dict(type='str', required=True),
            description=dict(type='str'),
            addresses=dict(type='list', elements='str', phpipam_name='namesrv1'),
            sections=dict(type='entity_list', controller='sections', phpipam_name='permissions', flatten=True, separator=';'),
        )
    )

    module_params = module.phpipam_params

    address_separator = ';'

    if not module.desired_absent:
        if module_params['addresses'] is not None:
            module_params['addresses'] = address_separator.join(module_params['addresses'])

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
