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
      - Subnet in CIDR notation
    required: true
    type: str
extends_documentation_fragment:
  - codeaffen.phpipam.phpipam
'''

EXAMPLES = '''
- name: "Create a subnet"
  cmeissner.phpipam.subnet:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    cidr: "192.0.2.128/25"
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

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamAnsibleModule


class PhpipamSubnetModule(PhpipamAnsibleModule):
    pass


def main():
    module = PhpipamAnsibleModule(
        argument_spec=dict(
            server_url=dict(type='str', required=True),
            app_id=dict(type='str', required=True),
            username=dict(type='str', required=True),
            password=dict(type='str', required=True),
            cidr=dict(type='str', required=True)
        )
    )

    module.connect()


if __name__ == "__main__":
    main()
