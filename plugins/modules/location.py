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
module: location
version_added: 1.4.0
short_description: Manage locations
description:
    - create, update and delete locations
author:
    - "Christian Meißner (@cmeissner)"
options:
    name:
        description: Name of the given location
        type: str
        required: true
    description:
        description: Description of the given location
        type: str
        required: false
    address:
        description:
            - Address of the given location
            - if I(resolv_location) is set to True, this address will be used to resolve the latitude and longitude
            - Mutually exclusive with latitude and longitude
        type: str
        required: false
    latitude:
        description:
            - Latitude of the given location
            - if I(resolv_location) is set to True, this latitude will be used to resolve the address
            - This parameter is mutually exclusive with address
            - This parameter is required if I(longitude) is given
        type: float
        required: false
    longitude:
        description:
            - Longitude of the given location
            - if I(resolv_location) is set to True, this longitude will be used to resolve the address
            - This parameter is mutually exclusive with address
            - This parameter is required if I(latitude) is given
        type: float
        required: false
    resolv_location:
        description:
            - Resolve the given location
            - Requires network connectivity to https://nominatim.org/ to resolve the given address
            - If address can not be resolved, latitude and longitude will not be set
        type: bool
        required: false
        default: no
requirements:
    - geopy
extends_documentation_fragment:
    - codeaffen.phpipam.phpipam
    - codeaffen.phpipam.phpipam.entity_state
'''

EXAMPLES = '''
- name: "Create with address"
  codeaffen.phpipam.location:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my location"
    description: "my location description"
    address: "my location address"
    state: present

- name: "Create location with geo coordinates"
  codeaffen.phpipam.location:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my location"
    description: "my location description"
    latitude: 123.456
    longitude: 123.456
    state: present

- name: "Remove location"
  codeaffen.phpipam.location:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    name: "my location"
    state: absent
'''

import traceback
from ansible_collections.codeaffen.phpipam.plugins.module_utils.phpipam_helper import PhpipamEntityAnsibleModule

try:
    from geopy.geocoders import Nominatim
    from geopy.point import Point
    HAS_GEOPY = True
except ImportError:
    HAS_GEOPY = False
    GEOPY_IMP_ERR = traceback.format_exc()


class PhpipamToolsLocationsModule(PhpipamEntityAnsibleModule):
    pass


def main():
    module = PhpipamToolsLocationsModule(
        phpipam_spec=dict(
            id=dict(type='int', invisible=True, phpipam_name='id'),
            name=dict(type='str', required=True),
            description=dict(type='str', required=False),
            address=dict(type='str', required=False),
            latitude=dict(type='float', required=False, phpipam_name='lat'),
            longitude=dict(type='float', required=False, phpipam_name='long'),
            resolv_location=dict(type='bool', required=False, default=False, api_invisible=True),
        ),
        mutually_exclusive=[['address', 'latitude'], ['address', 'longitude']],
        required_together=[['latitude', 'longitude']],
    )

    module_params = module.phpipam_params

    if module_params['resolv_location']:
        if not HAS_GEOPY:
            module.fail_json(msg='geopy is required for resolv_location', exception=GEOPY_IMP_ERR)

        geolocator = Nominatim(user_agent='ansible-phpipam-module')
        if 'address' in module_params and module_params['resolv_location']:
            location = geolocator.geocode(module_params['address'])
            if location:
                module_params['latitude'] = str(location.latitude)
                module_params['longitude'] = str(location.longitude)
        elif 'latitude' in module_params and 'longitude' in module_params:
            location = geolocator.reverse(Point(float(module_params['latitude']), float(module_params['longitude'])))
            if location:
                module_params['address'] = location.address
                module_params['latitude'] = str(location.latitude)
                module_params['longitude'] = str(location.longitude)

    with module.api_connection():
        module.run()


if __name__ == "__main__":
    main()
