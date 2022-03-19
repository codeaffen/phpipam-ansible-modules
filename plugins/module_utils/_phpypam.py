# -*- coding: utf-8 -*-
# (c) Christian Meißner 2022

# pylint: disable=raise-missing-from
# pylint: disable=super-with-arguments

from __future__ import absolute_import, division, print_function
__metaclassing__ = type

import traceback

try:
    import phpypam
    from phpypam import PHPyPAMEntityNotFoundException
    HAS_PHPIPAM = True
except ImportError:
    HAS_PHPIPAM = False
    PHPIPAM_IMP_ERR = traceback.format_exc()


class PhpipamAnsibleException(Exception):
    pass


class Api(object):
    """ Phpypam API bindings

    Provide an interface to interact with phpipam Api in a common manner.

    :param url: URL to the Phpypam API
    :type url: str
    :param app_id: App ID for the Phpypam API
    :type app_id: str
    :param username: Username to authenticate with
    :type username: str
    :param password: Password to authenticate with
    :type password: str
    :param ssl_verify: Whether to verify SSL certificates
    :type ssl_verify: bool
    """

    def __init__(self, **kwargs):
        """ Initialize the Phpypam API """
        self.phpipamapi = phpypam.api(**kwargs)

    def get_entity(self, **kwargs):
        """ Method to find an entity.

        :param controller: The controller
        :type controller: str
        :param kwarags: The parameters to use for the search
        :type kwarags: dict

        :return: The entity or `None` if no entity was found.
        """
        if 'path' in kwargs:
            entity = self._find_entity(kwargs['controller'], kwargs['path'], kwargs.get('params', None))
        elif 'subnet' in kwargs['controller']:
            entity = self._find_subnet(kwargs['subnet'], kwargs['mask'], kwargs['section'])
        elif 'address' in kwargs['controller']:
            # entity = self._find_address(kwargs['ipaddress'])
            entity = self._find_address(kwargs['ip'])
        elif 'device' in kwargs['controller']:
            entity = self._find_device(kwargs['hostname'])
        elif kwargs['controller'] == 'tools/device_type':
            entity = self._find_device_type(kwargs['name'])
        elif kwargs['controller'] == 'tools/tags':
            entity = self._find_by_key(kwargs['controller'], kwargs['value'], key='type')
        elif 'tools' in kwargs['controller'] or kwargs['controller'] in ['vlan', 'l2domain', 'vrf']:
            entity = self._find_by_key(kwargs['controller'], kwargs['name'])
        else:
            entity = self._find_entity(kwargs['controller'], '/' + kwargs['name'])

        return entity

    def _find_entity(self, controller, path, params=None):
        """ Method to find an entity.

        This is the generic method to find an entity.

        :param controller: The controller
        :type controller: str
        :param path: The path to the entity
        :type path: str
        :param params: The parameters to use for the search
        :type params: dict

        :return: The entity or `None` if no entity was found.
        :type return: dict
        """
        try:
            entity = self.phpipamapi.get_entity(controller=controller, controller_path=path, params=params)
        except PHPyPAMEntityNotFoundException:
            return None

        if isinstance(entity, list):
            if len(entity) == 1:
                entity = entity[0]
            else:
                self.fail_json(msg="Found no results while searching for {0} at {1}".format(controller, path))

        return entity

    def _find_subnet(self, subnet, mask, section):
        """ Method to find a subnet.

        To find a subnet we need a subnet, a bit mask and a section.

        :param subnet: The subnet to find
        :type subnet: str
        :param mask: The mask of the subnet
        :type mask: str
        :param section: The section of the subnet
        :type section: str

        :return: The subnet or `None` if no subnet was found.
        :type return: dict
        """
        path = 'cidr/{0}/{1}'.format(subnet, mask)

        lookup_params = {
            'filter_by': 'sectionId',
            'filter_value': self._find_entity('sections', section)['id'],
        }

        return self._find_entity('subnets', path, params=lookup_params)

    def _find_address(self, address):
        path = 'search/{0}'.format(address)
        return self._find_entity('addresses', path)

    def _find_device(self, hostname):
        return self._find_by_key('devices', hostname, key='hostname')

    def _find_device_type(self, device_type):
        result = self._find_by_key('tools/device_types', device_type, key='tname')
        if result and 'tid' in result:
            result['id'] = result['tid']
        return result

    def _find_vlan(self, vlan):
        return self._find_by_key(self.controller_uri, vlan)

    def _find_by_key(self, controller, value, key='name'):
        """
        Some controllers don't provide the ability to search for entities by uri
        so we need the possibility to search via url parameters.
        this is done by parameters `filter_by` and `filter_value` in phpIPAM API

        :param controller: which controller to use
        :param value: the value for which we are looking for
        :param key: the key which we use for `filter_by`. Default is `name`.

        :return: An entity or `None` if no entity was found.
        """
        lookup_params = {
            'filter_by': key,
            'filter_value': value,
        }
        return self._find_entity(controller, '/', params=lookup_params)

    def create_entity(self, controller, data):
        """
        Create an entity.

        :param controller: The controller
        :type controller: str
        :param data: The data to create
        :type data: dict

        :return: The created entity
        :type return: dict
        """
        try:
            self.phpipamapi.create_entity(controller=controller, data=data)
            entity = self.get_entity(controller=controller, **data)
        except PHPyPAMEntityNotFoundException:
            entity = None

        return entity

    def update_entity(self, controller, entity_id, desired_entity, current_entity):
        """ Methode to update an entity.

        :param controller: The controller
        :type controller: str
        :param desired_entity: The desired entity
        :type desired_entity: dict
        :param current_entity: The current entity
        :type current_entity: dict

        :return: The updated entity
        :type return: dict
        """

        # There is a bug in l2domains controller. If we query a domain we get `sections`
        # but if we want to set sections the controller expects `permissions`.
        # This is not the best place to do it but we didn't expect a quick fix from phpIPAM developers.
        # https://github.com/phpipam/phpipam/issues/3190
        if 'l2domain' in controller and 'permissions' in desired_entity:
            current_entity['permissions'] = current_entity['sections']

        updated_entity = {k: v for k, v in desired_entity.items() if v != current_entity[k] and k != 'parent'}

        # entity_id = 'id' in self.phpipam_spec and self.phpipam_spec['id']['phpipam_name'] or 'id'

        if updated_entity:
            if 'tools' not in controller:
                updated_entity[entity_id] = current_entity[entity_id]
            if controller == 'vlan':
                updated_entity['name'] = current_entity['name']
        else:
            return current_entity

        if 'tools' in controller or controller in ['vlan', 'vrf']:
            update_path = current_entity[entity_id]
        else:
            update_path = '/'

        self.phpipamapi.update_entity(controller, update_path, updated_entity)

        try:
            entity = self.get_entity(controller=controller, **updated_entity)
        except PHPyPAMEntityNotFoundException:
            entity = None

        return entity

    def delete_entity(self, controller, entity_id, current_entity):
        """ Method to delete an entity.

        :param controller: The controller
        :type controller: str
        :param entity_id: The id of the entity
        :type entity_id: str
        :param current_entity: The current entity
        :type current_entity: dict

        :return: None
        """
        try:
            self.phpipamapi.delete_entity(controller, current_entity[entity_id])
        except PHPyPAMEntityNotFoundException:
            raise PhpipamAnsibleException("Entity '{0}' of type '{1}' can't be ensured absentd:\n{2}".format(current_entity['name'], controller, traceback.format_exc()))

        return None

    def resolve_entity(self, params, key):
        if key not in params:
            return None

        entity_spec = self.phpipam_spec[key]

        controller = entity_spec['controller'] or self.controller_uri

        result = None
        if controller == 'subnets':
            subnet, mask = params[key].split('/')
            result = self.find_subnet(subnet, mask, params['section'])
        elif controller == 'tools/device_types':
            result = self.find_device_type(params[key])
        elif controller == 'tools/tags':
            result = self.find_by_key(controller=controller, value=params[key], key='type')
        elif 'tools' in controller or controller in ['vlan', 'l2domains', 'vrf']:
            result = self.find_by_key(controller=controller, value=params[key])
        else:
            if entity_spec.get('type') == 'entity':
                result = self.find_entity(controller=controller, path='/' + params[key])
            elif entity_spec.get('type') == 'entity_list':
                flatten = entity_spec.get('flatten', False)
                if flatten:
                    flatten_result = [self.find_entity(controller=controller, path='/' + e)['id'] for e in params[key]]
                    result = entity_spec.get('separator', ';').join(flatten_result)
            else:
                result = [self.find_entity(controller=controller, path='/' + value) for value in params[key]]

        self.set_entity(key)

        return result
