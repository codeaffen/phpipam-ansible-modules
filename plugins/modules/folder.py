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
module: folder
version_added: 1.7.0
short_description: Manage folders
description:
    - create, update and delete folders
author:
    - "Christian Meißner (@cmeissner)"
options:
    name:
        description: Name of the folder to manage
        type: str
        required: false
    section:
        description: Name of the section under which the folder is located
        type: int
        required: true
    parent:
        description: Name of parent folder
        type: str
        required: false
    permissions:
        description: JSON object that represent the permissions for each user
        type: json
        required: false
        default: None
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
    name: "Example folder"
    section: "EXAMPLE INC"
    state: present

- name: "Create a folder with parent"
  codeaffen.phpipam.folder:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    folder: "Example sub folder"
    parent: "Example folder"
    section: "DEVOPS department"
    state: present
'''

RETURN = '''
entity:
    description: Final state of the affected entities grouped by their type.
    returned: success
    type: dict
    contains:
        folders:
            description: List of folders.
            type: list
            elements: dict
'''

from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule


class PhpipamFolderModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamFolderModule(
        phpipam_spec=dict(
            name=dict(type='str', phpipam_name='description'),
            section=dict(type='entity', required=True, controller='sections', phpipam_name='sectionId'),
            parent=dict(type='entity', phpipam_name='masterSubnetId'),
            permissions=dict(type='json'),
            is_folder=dict(type='bool', default=True),
        ),
    )

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
