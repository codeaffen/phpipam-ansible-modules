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

.. _ansible_collections.codeaffen.phpipam.address_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

codeaffen.phpipam.address module -- Manage addresses
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `codeaffen.phpipam collection <https://galaxy.ansible.com/codeaffen/phpipam>`_ (version 1.7.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install codeaffen.phpipam`.

    To use it in a playbook, specify: :code:`codeaffen.phpipam.address`.

.. version_added

.. versionadded:: 0.2.0 of codeaffen.phpipam

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- create, update and delete addresses


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
        <div class="ansibleOptionAnchor" id="parameter-app_id"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-app_id:

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
        <div class="ansibleOptionAnchor" id="parameter-description"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-description:

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

      Address description


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-device"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-device:

      .. rst-class:: ansible-option-title

      **device**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-device" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Device address belongs to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-exclude_ping"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-exclude_ping:

      .. rst-class:: ansible-option-title

      **exclude_ping**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-exclude_ping" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Exclude this address from status update scans


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hostname"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-hostname:

      .. rst-class:: ansible-option-title

      **hostname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Address hostname


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignore_ptr"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-ignore_ptr:

      .. rst-class:: ansible-option-title

      **ignore_ptr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignore_ptr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls if PTR should not be created


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ipaddress"></div>
        <div class="ansibleOptionAnchor" id="parameter-ip"></div>
        <div class="ansibleOptionAnchor" id="parameter-address"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-address:
      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-ip:
      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-ipaddress:

      .. rst-class:: ansible-option-title

      **ipaddress**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ipaddress" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-aliases:`aliases: ip, address`

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address to hanle


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_gateway"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-is_gateway:

      .. rst-class:: ansible-option-title

      **is_gateway**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-is_gateway" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines if address is presented as gateway


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mac_address"></div>
        <div class="ansibleOptionAnchor" id="parameter-mac"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-mac:
      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-mac_address:

      .. rst-class:: ansible-option-title

      **mac_address**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mac_address" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-aliases:`aliases: mac`

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Mac address


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-note"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-note:

      .. rst-class:: ansible-option-title

      **note**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-note" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Note


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-owner"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-owner:

      .. rst-class:: ansible-option-title

      **owner**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-owner" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Address owner


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-password:

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
        <div class="ansibleOptionAnchor" id="parameter-port"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-port:

      .. rst-class:: ansible-option-title

      **port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Port


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ptr"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-ptr:

      .. rst-class:: ansible-option-title

      **ptr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ptr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      DNS PTR record


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-section"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-section:

      .. rst-class:: ansible-option-title

      **section**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-section" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      :ansible-option-versionadded:`added in 1.3.1 of codeaffen.phpipam`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      name of the section the given subnet belongs to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-server_url"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-server_url:

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
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-state:

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

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-subnet:

      .. rst-class:: ansible-option-title

      **subnet**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-subnet" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      subnet address belongs to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tag"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-tag:

      .. rst-class:: ansible-option-title

      **tag**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tag" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP tag (online, offline, ...)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-username:

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

      .. _ansible_collections.codeaffen.phpipam.address_module__parameter-validate_certs:

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


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Reserve an IP address"
      codeaffen.phpipam.address:
        username: "admin"
        password: "s3cr3t"
        server_url: "https://ipam.example.com"
        address: "192.0.2.1"
        section: "Customers"
        description: "Default router of sunet"
        subnet: "192.0.2.0/24"
        is_gateway: yes
        state: present

    - name: "Remove address reservation"
      codeaffen.phpipam.address:
        username: "admin"
        password: "s3cr3t"
        server_url: "https://ipam.example.com"
        address: "192.0.2.1"
        subnet: "192.0.2.0/24"
        section: "Customers"
        state: absent




.. Facts


.. Return values


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

