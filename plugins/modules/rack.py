#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Christian Meißner 2023
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
module: rack
version_added: 1.8.0
short_description: Manage racks
description:
    - create, update and delete racks
author:
    - "Christian Meißner (@cmeissner)"
notes:
    - This module needs a phpIPAM backend with version 1.3 or highter.

options:
    name:
        description: Name of the rack to manage
        type: str
        required: true
    description:
        description: A short optional description for the given rack
        type: str
        required: false
    customer:
        Description: The customer name to which the rack belongs to
        type: str
        required: false
    location:
        description: Name of the location where the rack can be found
        type: str
        required: false
    units:
        description: Amount of available units in the given rack
        type: int
        required: false
        default: 42
    row:
        description: Row where to find the rack
        type: int
        required: false
        default: 1
    has_back:
        description: Does the rack have a accessible back side
        type: bool
        required: false
        default: false
    top_down:
        description: Counting units from top to down
        type: bool
        required: false
        default: true
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create a folder"
  codeaffen.phpipam.folder:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "Example rack"
    Customer: "EXAMPLE INC"
    state: present

- name: "Create a folder with parent"
  codeaffen.phpipam.folder:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "Example rack"
    Customer: "EXAMPLE INC"
    units: 22
    state: present
'''

RETURN = '''
entity:
    description: Final state of the affected entities grouped by their type.
    returned: success
    type: dict
    contains:
        racs:
            description: List of racks.
            type: list
            elements: dict
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamRackModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamRackModule(
        phpipam_spec=dict(
            name=dict(type='str', required=True),
            description=dict(type='str'),
            customer=dict(type='entity', controller='customer', phpipam_name='customer_id'),
            location=dict(type='entity', controller='location'),
            untis=dict(type='int', required=True, default=42, phpipam_name='size'),
            row=dict(type='int', default=1),
            has_back=dict(type='bool', default=False, phpipam_name='hasBack'),
            top_down=dict(type='bool', default=True, phpipam_name='topDown'),
        ),
    )

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
