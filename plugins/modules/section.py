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
        example: "customer_1"
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
        argument_spec=dict(
            name=dict(type='str', required=True),
            description=dict(type='str', required=False),
            parent=dict(type='str', required=False, defautl=None),
        )
    )

    if not module.desired_absent:
        pass

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
