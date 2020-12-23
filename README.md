# phpIPAM Ansible Modules

![Version on Galaxy](https://img.shields.io/badge/dynamic/json?style=flat&label=galaxy&prefix=v&url=https://galaxy.ansible.com/api/v2/collections/codeaffen/phpipam/&query=latest_version.version)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/0372c2bb95e845ce96fa5d4cf13ca1ca)](https://www.codacy.com/gh/codeaffen/phpipam-ansible-modules/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=codeaffen/phpipam-ansible-modules&amp;utm_campaign=Badge_Grade)
[![Documentation Status](https://readthedocs.org/projects/phpipam-ansible-modules/badge/?version=develop)](https://phpipam-ansible-modules.readthedocs.io/en/develop/?badge=develop)

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

Current documentation can be found on [readthedocs.io](https://phpipam-ansible-modules.readthedocs.io/en/develop/).

### ansible-doc

If you have installed the collection you can facilitate `ansible-doc` to display documentation for a given module.

```bash
ansible-doc codeaffen.phpipam.section
```

### repository folder

A last option to read the docs is the docs folder in this repository.

## Dependencies

The following dependencies have to be fulfiled by the Ansible controller.

* inflection
* ipaddress
* phpypam>=1.0.0

## Need help?

If you’ve found any issues in this release please head over to github and open a bug so we can take a look.
