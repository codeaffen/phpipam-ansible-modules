# phpIPAM Ansible Modules

[![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv3%2Fplugin%2Fansible%2Fcontent%2Fpublished%2Fcollections%2Findex%2Fcodeaffen%2Fphpipam%2F&query=%24.highest_version.version&label=galaxy)](https://galaxy.ansible.com/ui/repo/published/codeaffen/phpipam/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/0372c2bb95e845ce96fa5d4cf13ca1ca)](https://www.codacy.com/gh/codeaffen/phpipam-ansible-modules/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=codeaffen/phpipam-ansible-modules&amp;utm_campaign=Badge_Grade)
[![Documentation Status](https://readthedocs.org/projects/phpipam-ansible-modules/badge/?version=develop)](https://phpipam-ansible-modules.readthedocs.io/en/develop/?badge=develop)

This collection provides modules to manage entities in a [phpIPAM](https://phpipam.net/). This is neither a collection of roles nor playbooks. It provides modules to write your own roles and/or playbooks.

We get a lot of inspiration from [foreman-ansible-modules](https://galaxy.ansible.com/theforeman/foreman) for our modules.

## Installation

The collection is available via [Ansible Galaxy](https://galaxy.ansible.com/ui/repo/published/codeaffen/phpipam/). So you can run

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

* colour
* geopy
* inflection
* ipaddress
* phpypam>=1.0.0

## Compatibility notice

To ensure `phpipam-ansible-modules` work correctly with phpIPAM versions 1.7 and above, you need to modify the phpIPAM configuration to stringify API results. This is crucial because newer phpIPAM versions might return numerical values directly, which the Ansible modules might expect as strings.

Here's how to implement the workaround:

**1. Modify phpIPAM Configuration**

You need to set the `api_stringify_results` variable to `true` in your phpIPAM configuration. This change should be made in the `config.php` file, which is typically located in the phpIPAM installation directory (e.g., `/var/www/html/phpipam/config.php` or `/var/www/phpipam/config.php`).

Add or modify the following line in your `config.php` file:

```
<?php
/*
 * phpIPAM config.php
 *
 * ... existing configuration ...
 */

// Required for Ansible modules with phpIPAM v1.7 and above
$api_stringify_results = true;

/*
 * ... rest of your configuration ...
 */
?>
```
## Need help?

If you’ve found any issues in this release please head over to github and open a bug so we can take a look.
