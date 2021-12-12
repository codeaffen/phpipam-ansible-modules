#!/usr/bin/env python

# -*- coding: utf-8 -*-
# (c) Christian Meißner 2021
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
module: tag
version_added: 1.4.0
short_description: Manage tags
description:
    - create, update and delete tags
author:
    - "Christian Meißner (@cmeissner)"
options:
    name:
        description: Name of the given tag
        type: str
        required: true
        aliases: [type]
    show_tag:
        description: Show tag or not
        type: bool
        required: false
        default: no
    bg_color:
        description:
            - Background color of the given tag
            - Can be a valid color name or a hex code
        type: str
        required: true
    fg_color:
        description:
            - Foreground color of the given tag
            - Can be a valid color name or a hex code
        type: str
        required: true
    compress_range:
        description: Compress range or not
        type: bool
        required: false
        default: no
    update_tags:
        description: Update tags or not
        type: bool
        required: false
        default: no
    is_locked:
        description: Lock tag or not
        type: bool
        required: false
        default: no
requirements:
    - colour
    - inflection
    - ipaddress
    - phpypam>=1.0.0
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create tag"
  codeaffen.phpipam.tag:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my tag"
    bg_color: #ffffff
    fg_color: #000000
    state: present

- name: "Remove tag"
  codeaffen.phpipam.tag:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my tag"
    state: absent
'''

import traceback
from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule, missing_required_lib
try:
    from colour import Color
    HAS_COLOUR = True
except ImportError:
    HAS_COLOUR = False
    COLOUR_IMP_ERR = traceback.format_exc()


class PhpipamToolsTagsModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamToolsTagsModule(
        phpipam_spec=dict(
            id=dict(type='int', invisible=True, phpipam_name='id'),
            name=dict(type='str', required=True, aliases=['type'], phpipam_name='type'),
            show_tag=dict(type='bool', required=False, default=False, phpipam_name='showtag'),
            bg_color=dict(type='str', required=True, phpipam_name='bgcolor'),
            fg_color=dict(type='str', required=True, phpipam_name='fgcolor'),
            compress_range=dict(type='bool', default=False),
            update_tags=dict(type='bool', required=False, default=False, phpipam_name='updateTag'),
            is_locked=dict(type='bool', default='no'),
        )
    )

    def get_color_code(color):
        try:
            c = Color(color)
            return c.get_hex()
        except ValueError:
            module.fail_json(msg="Invalid color: {}".format(color))

    if not HAS_COLOUR:
        module.fail_json(msg=missing_required_lib("colour"), exception=COLOUR_IMP_ERR)

    module_params = module.phpipam_params

    module_params['bg_color'] = get_color_code(module_params['bg_color'])
    module_params['fg_color'] = get_color_code(module_params['fg_color'])
    module_params['locked'] = 'yes' if module_params['is_locked'] else 'no'
    module_params['compress'] = 'yes' if module_params['compress_range'] else 'no'

    del(module_params['is_locked'])
    del(module_params['compress_range'])

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
