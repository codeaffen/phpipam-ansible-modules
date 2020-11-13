# Copyright (c) 2020 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import ipaddress


class FilterModule(object):

    """Define useful filter in collection."""

    def filters(self):
        """Export filter for ansible.

        :return: return a dictionary of filters
        :rtype: dict
        """
        return {
            'is_subnet': is_subnet,
        }


def is_subnet(children, parent):
    """Check if a subnet belongs to another.

    First argument is a subnet  second another. If the first subnet belongs to second

    :param children: [description]
    :type children: [type]
    :param parent: [description]
    :type parent: [type]
    :return: [description]
    :rtype: [type]
    """
    c = ipaddress.ip_network(children)
    p = ipaddress.ip_network(parent)

    if not c.subnet_of(p) or c == p:
        return False
    else:
        return c.subnet_of(p)
