# phpIPAM Ansible Modules

This collection provides modules to manage entities in a [phpIPAM](https://phpipam.net/). This is neighter a collection of roles nor playbooks. It provides modules to wrote your own roles and/or playbooks.

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
$ ansible-doc codeaffen.phpipam.section
> SECTION    (/home/user/ansible_collections/codeaffen/phpipam/plugins/modules/section.py)

        create, update and delete sections

  * This module is maintained by The Ansible Community
OPTIONS (= is mandatory):

- app_id
        API app name
        [Default: ansible]
        type: str

- description
        Short describtive text
        [Default: None]
        type: str

- dns_resolver
        The NS resolver to be used for this section
        [Default: (null)]
        type: str

- list_order
        Order in sections list view
        [Default: (null)]
        type: int

= name
        Name of the section

        example: customer_1
        type: str

- parent
        Name of the parent section
        (Aliases: master, master_section)[Default: None]
        type: str

= password
        Password of the user to access phpIPAM server

        type: str

- permissions
        JSON object that represent the permissions for each user
        [Default: None]
        type: json

= server_url
        URL of the phpIPAM server

        type: str

- show_supernets_only
        Show only supernets in sebnet list view
        [Default: False]
        type: bool

- show_vlan
        Show/hide VLANs in subnet list view
        [Default: False]
        type: bool

- show_vrf
        Show/hide VRFs in subnet list view
        [Default: False]
        type: bool

- state
        State of the entity
        (Choices: present, absent)[Default: present]
        type: str

- strict_mode
        If set to true, consistency of subnets and IP addresses will be checked
        [Default: False]
        type: bool

- subnet_ordering
        How to order subnets within this section
        [Default: subnet,asc]
        type: str

= username
        Username to access phpIPAM server

        type: str


REQUIREMENTS:  inflection, ipaddress, phpypam>=1.0.0

AUTHOR: Christian Meißner (@cmeissner)
        METADATA:
          status:
          - preview
          supported_by: community


EXAMPLES:

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
```

### repository folder

A last option to read the docs is the docs folder in this repository.

## Dependencies

The following dependencies have to be fulfiled by the Ansible controller.

* inflection
* ipaddress
* phpypam>=1.0.0
