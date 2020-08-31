# (c) Christian Meißner <cme+ansible@meissner.sh>, 2020
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

class ModuleDocFragment(object):

  # phpIPAM documentation fragment
  DOCUMENTATION = '''
requirements:
  - phpipam-client
options:
  server_url:
    description: URL of the phpIPAM server
    required: true
    type: str
  app_id:
    description: API app name
    required: false
    default: ansible
    type: str
  username:
    description: Username to access phpIPAM server
    required: true
    type: str
  password:
    description: Password of the user to access phpIPAM server
    required: true
    type: str
'''
