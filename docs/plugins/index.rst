

.. meta::
  :antsibull-docs: 2.5.0


.. _plugins_in_codeaffen.phpipam:

Codeaffen.Phpipam
=================

Collection version 1.7.0

.. contents::
   :local:
   :depth: 1

Description
-----------

Ansible Modules to manage phpIPAM installations

**Authors:**

* Andreas Klamke <andy@klamke.net>
* Billy Longman <bill.longman@summit-broadband.com>
* Christian Meißner <cme@codeaffen.org>
* Gerald-Markus Zabos <gmzabos@users.noreply.github.com>
* Mario Fritschen <github@fritschen.net>
* Scott Arthur <scott@scottatron.com>
* lush <porous@web.de>

**Supported ansible-core versions:**

* 2.9 or newer

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/codeaffen/phpipam-ansible-modules/issues"
    external: true
  - title: "Homepage"
    url: "https://codeaffen.org/projects/phpipam-ansible-modules"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/codeaffen/phpipam-ansible-modules"
    external: true




.. toctree::
    :maxdepth: 1


Plugin Index
------------

These are the plugins in the codeaffen.phpipam collection:


Modules
~~~~~~~

* :ansplugin:`address module <codeaffen.phpipam.address#module>` -- Manage addresses
* :ansplugin:`device module <codeaffen.phpipam.device#module>` -- Manage devices
* :ansplugin:`device_type module <codeaffen.phpipam.device_type#module>` -- Manage device types
* :ansplugin:`domain module <codeaffen.phpipam.domain#module>` -- Manage L2 routing domains
* :ansplugin:`folder module <codeaffen.phpipam.folder#module>` -- Manage folders
* :ansplugin:`location module <codeaffen.phpipam.location#module>` -- Manage locations
* :ansplugin:`nameserver module <codeaffen.phpipam.nameserver#module>` -- Manage nameservers
* :ansplugin:`section module <codeaffen.phpipam.section#module>` -- Manage sections
* :ansplugin:`subnet module <codeaffen.phpipam.subnet#module>` -- Manage subnets
* :ansplugin:`tag module <codeaffen.phpipam.tag#module>` -- Manage tags
* :ansplugin:`vlan module <codeaffen.phpipam.vlan#module>` -- Manage vlans
* :ansplugin:`vrf module <codeaffen.phpipam.vrf#module>` -- Manage virtual routers and forwarders

.. toctree::
    :maxdepth: 1
    :hidden:

    address_module
    device_module
    device_type_module
    domain_module
    folder_module
    location_module
    nameserver_module
    section_module
    subnet_module
    tag_module
    vlan_module
    vrf_module


Filter Plugins
~~~~~~~~~~~~~~

* :ansplugin:`is_subnet filter <codeaffen.phpipam.is_subnet#filter>` -- Check if a subnet belongs to another

.. toctree::
    :maxdepth: 1
    :hidden:

    is_subnet_filter


