.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-entry
.. role:: ansible-option-default
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.codeaffen.phpipam.subnet_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

codeaffen.phpipam.subnet module -- Manage subnets
+++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `codeaffen.phpipam collection <https://galaxy.ansible.com/codeaffen/phpipam>`_ (version 1.6.1).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install codeaffen.phpipam`.

    To use it in a playbook, specify: :code:`codeaffen.phpipam.subnet`.

.. version_added

.. versionadded:: 0.0.1 of codeaffen.phpipam

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- create, update and delete subnets


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- inflection
- ipaddress
- phpypam>=1.0.0






.. Options

Parameters
----------


.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-allow_requests"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-allow_requests:

      .. rst-class:: ansible-option-title

      **allow_requests**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allow_requests" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls if IP requests are allowed for subnet


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-app_id"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-app_id:

      .. rst-class:: ansible-option-title

      **app_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-app_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      API app name


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"ansible"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cidr"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-cidr:

      .. rst-class:: ansible-option-title

      **cidr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cidr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Network in CIDR format.

      Mutually exclusive with \ :emphasis:`subnet`\  and \ :emphasis:`mask`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-description"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-description:

      .. rst-class:: ansible-option-title

      **description**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Text which is shown in side bar if 'show as name' is selected


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-discover_subnet"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-discover_subnet:

      .. rst-class:: ansible-option-title

      **discover_subnet**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-discover_subnet" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls if new hosts should be discovered for new host scans


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dns_records"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-dns_records:

      .. rst-class:: ansible-option-title

      **dns_records**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dns_records" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls whether hostname DNS records are displayed


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dns_recursive"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-dns_recursive:

      .. rst-class:: ansible-option-title

      **dns_recursive**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dns_recursive" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls if PTR records should be created for subnet


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_folder"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-is_folder:

      .. rst-class:: ansible-option-title

      **is_folder**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-is_folder" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls if we are adding subnet or folder

      can't be changed after subnet was created


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_full"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-is_full:

      .. rst-class:: ansible-option-title

      **is_full**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-is_full" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Marks subnet as used


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-linked_subnet"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-linked_subnet:

      .. rst-class:: ansible-option-title

      **linked_subnet**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-linked_subnet" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Linked ipv6 subnet in CIDR format


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-location"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-location:

      .. rst-class:: ansible-option-title

      **location**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-location" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Subnet location


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mask"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-mask:

      .. rst-class:: ansible-option-title

      **mask**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mask" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Prefix length (bits) for ipv4 and ipv6 subnets.

      Mutually exclusive with \ :emphasis:`cidr`\ .

      If set. \ :emphasis:`subnet`\  is required.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nameserver"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-nameserver:

      .. rst-class:: ansible-option-title

      **nameserver**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nameserver" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the DNS server which should attach to subnet


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-parent"></div>
        <div class="ansibleOptionAnchor" id="parameter-master_subnet_cidr"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-master_subnet_cidr:
      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-parent:

      .. rst-class:: ansible-option-title

      **parent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-parent" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-aliases:`aliases: master_subnet_cidr`

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      CIDR of parent subnet


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password of the user to access phpIPAM server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-permissions"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-permissions:

      .. rst-class:: ansible-option-title

      **permissions**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-permissions" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`json`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      JSON object that represent the permissions for each user


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"None"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ping_subnet"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-ping_subnet:

      .. rst-class:: ansible-option-title

      **ping_subnet**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ping_subnet" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls if subnet should be included in status checks


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-routing_domain"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-routing_domain:

      .. rst-class:: ansible-option-title

      **routing_domain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-routing_domain" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      :ansible-option-versionadded:`added in 1.6.0 of codeaffen.phpipam`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Layer-2 routing domain the vlan belongs to

      If you have \ :emphasis:`vlan`\  with same number in different routing domains it need to be set on desired value


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"default"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scan_agent"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-scan_agent:

      .. rst-class:: ansible-option-title

      **scan_agent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scan_agent" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of scanagent which should be used for subnet


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-section"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-section:

      .. rst-class:: ansible-option-title

      **section**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-section" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the section under which the subnet is located


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-server_url"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-server_url:

      .. rst-class:: ansible-option-title

      **server_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-server_url" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL of the phpIPAM server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show_as_name"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-show_as_name:

      .. rst-class:: ansible-option-title

      **show_as_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show_as_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If this is set to 'true' description is shown in side bar instead of CIDR


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of the entity


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`present` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`absent`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-subnet"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-subnet:

      .. rst-class:: ansible-option-title

      **subnet**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-subnet" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Network address

      Mutually exclusive with \ :emphasis:`cidr`\ .

      If set, \ :emphasis:`mask`\  is required.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-subnet_state"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-subnet_state:

      .. rst-class:: ansible-option-title

      **subnet_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-subnet_state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Assigned tag of the subnet.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-threshold"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-threshold:

      .. rst-class:: ansible-option-title

      **threshold**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-threshold" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Subnet threshold


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-username:

      .. rst-class:: ansible-option-title

      **username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Username to access phpIPAM server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-validate_certs:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Is the TLS certificate of the phpIPAM server verified or not.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-default-bold:`yes` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-vlan"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-vlan:

      .. rst-class:: ansible-option-title

      **vlan**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vlan" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      VLAN which the subnet should belongs to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-vrf"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__parameter-vrf:

      .. rst-class:: ansible-option-title

      **vrf**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vrf" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      VRF which the sunet should belongs to


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Create a subnet"
      codeaffen.phpipam.subnet:
        username: "admin"
        password: "s3cr3t"
        server_url: "https://ipam.example.com"
        cidr: "192.0.2.128/26"
        section: "EXAMPLE INC"
        state: present

    - name: "Create a subnet with parent"
      codeaffen.phpipam.subnet:
        username: "admin"
        password: "s3cr3t"
        server_url: "https://ipam.example.com"
        cidr: "192.0.2.128/28"
        parent: "192.0.2.128/25"
        section: "DEVOPS department"
        state: present




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-entity"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__return-entity:

      .. rst-class:: ansible-option-title

      **entity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-entity" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Final state of the affected entities grouped by their type.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-entity/subnets"></div>

      .. _ansible_collections.codeaffen.phpipam.subnet_module__return-entity/subnets:

      .. rst-class:: ansible-option-title

      **subnets**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-entity/subnets" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of subnets.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>




..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Christian Meißner (@cmeissner)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/codeaffen/phpipam-ansible-modules/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://codeaffen.org/projects/phpipam-ansible-modules" aria-role="button" target="_blank" rel="noopener external">Homepage</a>
    <a href="https://github.com/codeaffen/phpipam-ansible-modules" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

