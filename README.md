# phpipam-ansible-modules

## work in progress

**This modules are still in development and not for production purpose. If we think you can use is in a more productive manner we will inform you.**

This collections provides modules to manage entities in a [phpIPAM](https://phpipam.net/). This is neighter a collection of roles nor playbooks. It provides modules to wrote your own roles and/or playbooks.

We get a lot of inspiration from [foreman-ansible-modules](https://galaxy.ansible.com/theforeman/foreman) for our modules.

## Installation

The collection is available via [Ansible Galaxy](https://galaxy.ansible.com/codeaffen/phpipam). So you can run

```bash
ansible-galaxy collection install codeaffen.phpipam
```

Alternatively you can build and install the collection from source.

```bash
make dist
ansible-galaxy collection install codeaffen-phpipam-<version>.tar.gz
```

## Documentation

### readthedocs.io

Current documentation can be found on [readthedocs.io](https://phpipam-ansible-modules.readthedocs.io/en/latest/).

### ansible-doc

If you have installed the collection you can facilitate `ansible-doc` to display documentation for a given module.

```bash
$ ansible-doc codeaffen.phpipam.subnet
> SUBNET    (/home/user/ansible_collections/codeaffen/phpipam/plugins/modules/subnet.py)

        create, update and delete subnets

  * This module is maintained by The Ansible Community
OPTIONS (= is mandatory):

- app_id
        API app name
        [Default: ansible]
        type: str

= cidr
        Subnet in CIDR notation

        type: str

= password
        Password of the user to access phpIPAM server

        type: str

= server_url
        URL of the phpIPAM server

        type: str

= username
        Username to access phpIPAM server

        type: str


REQUIREMENTS:  phpipam-client

AUTHOR: Christian Meißner (@cmeissner)
        METADATA:
          status:
          - preview
          supported_by: community


EXAMPLES:

- name: "Create a subnet"
  cmeissner.phpipam.subnet:
    username: "admin"
    password: "s3cr3t"
    server_url: "https://ipam.example.com"
    cidr: "192.0.2.128/25"
    state: present


RETURN VALUES:

entity:
  description: Final state of the affected entities grouped by their type.
  returned: success
  type: dict
  contains:
    subnets:
      description: List of subnets.
      type: list
      elements: dicts
```

### repository folder

A last option to read the docs is the [docs](docs) folder in this repository.

## Dependencies

The following dependencies have to be fulfiled by the Ansible controller.

* phpipam-client
* PyYAML
