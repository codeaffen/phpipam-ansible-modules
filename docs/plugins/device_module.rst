
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

.. _ansible_collections.codeaffen.phpipam.device_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

codeaffen.phpipam.device module -- Manage devices
+++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `codeaffen.phpipam collection <https://galaxy.ansible.com/codeaffen/phpipam>`_ (version 1.5.0).

    To install it, use: :code:`ansible-galaxy collection install codeaffen.phpipam`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.codeaffen.phpipam.device_module_requirements>` for details.

    To use it in a playbook, specify: :code:`codeaffen.phpipam.device`.

.. version_added

.. versionadded:: 0.5.0 of codeaffen.phpipam

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- create, update and delete devices


.. Aliases


.. Requirements

.. _ansible_collections.codeaffen.phpipam.device_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- inflection
- ipaddress
- phpypam\>=1.0.0






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

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-app_id:

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

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-description:

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

      A descriptive text for that entity


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hostname"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-hostname:

      .. rst-class:: ansible-option-title

      **hostname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Hostname of the given device


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ipaddress"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-ipaddress:

      .. rst-class:: ansible-option-title

      **ipaddress**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ipaddress" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the given device


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-password:

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
        <div class="ansibleOptionAnchor" id="parameter-rack"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-rack:

      .. rst-class:: ansible-option-title

      **rack**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rack" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Rack where the device belongs to.

      If set \ :emphasis:`starting\_rack\_unit`\  and \ :emphasis:`rack\_units`\  are also required.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rack_units"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-rack_units:

      .. rst-class:: ansible-option-title

      **rack_units**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rack_units" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Size of device in \ :emphasis:`U`\ .

      If set \ :emphasis:`rack`\  and \ :emphasis:`starting\_rack\_unit`\  are also required.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sections"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-sections:

      .. rst-class:: ansible-option-title

      **sections**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sections" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of sections where the device belongs to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-server_url"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-server_url:

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
        <div class="ansibleOptionAnchor" id="parameter-snmp_community"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_community:

      .. rst-class:: ansible-option-title

      **snmp_community**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_community" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The SNMP community string


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_port"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_port:

      .. rst-class:: ansible-option-title

      **snmp_port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_port" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The used SNMP port


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"161"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_queries"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_queries:

      .. rst-class:: ansible-option-title

      **snmp_queries**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_queries" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_timeout"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_timeout:

      .. rst-class:: ansible-option-title

      **snmp_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_timeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The SNMP connection timeout


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_v3_auth_pass"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_v3_auth_pass:

      .. rst-class:: ansible-option-title

      **snmp_v3_auth_pass**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_v3_auth_pass" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The password to authenticate via SNMPv3


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_v3_auth_protocol"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_v3_auth_protocol:

      .. rst-class:: ansible-option-title

      **snmp_v3_auth_protocol**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_v3_auth_protocol" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The used SNMPv3 auth protocol


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_v3_ctx_engine_id"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_v3_ctx_engine_id:

      .. rst-class:: ansible-option-title

      **snmp_v3_ctx_engine_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_v3_ctx_engine_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      CTX engine id when using SNMPv3


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_v3_ctx_name"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_v3_ctx_name:

      .. rst-class:: ansible-option-title

      **snmp_v3_ctx_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_v3_ctx_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      CTX name when using SNMPv3


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_v3_priv_pass"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_v3_priv_pass:

      .. rst-class:: ansible-option-title

      **snmp_v3_priv_pass**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_v3_priv_pass" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The password to authenticate via SNMPv3 in privacy mode


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_v3_priv_protocol"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_v3_priv_protocol:

      .. rst-class:: ansible-option-title

      **snmp_v3_priv_protocol**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_v3_priv_protocol" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The used SNMPv3 privacy protocol


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_v3_sec_level"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_v3_sec_level:

      .. rst-class:: ansible-option-title

      **snmp_v3_sec_level**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_v3_sec_level" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The used SNMPv3 security level


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmp_version"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-snmp_version:

      .. rst-class:: ansible-option-title

      **snmp_version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmp_version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The used SNMP version


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-starting_rack_unit"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-starting_rack_unit:

      .. rst-class:: ansible-option-title

      **starting_rack_unit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-starting_rack_unit" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Which is the starting rack unit where the device is mounted.

      If set \ :emphasis:`rack`\  and \ :emphasis:`racK\_units`\  are also required.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-state:

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
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Device type of this device.

      The value has to reflect values from device types configured.

      Default device types are \ :emphasis:`Switch`\ , \ :emphasis:`Router`\ , \ :emphasis:`Firewall`\ , \ :emphasis:`Hub`\ , \ :emphasis:`Wireless`\ , \ :emphasis:`Database`\ , \ :emphasis:`Workstation`\ , \ :emphasis:`Laptop`\  and \ :emphasis:`Other`\ .

      User defined types can be created either via UI, API (e.g. \ :emphasis:`device\_type`\  ansible module within this collection).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-username:

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

      .. _ansible_collections.codeaffen.phpipam.device_module__parameter-validate_certs:

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

      - :ansible-option-choices-entry:`false`
      - :ansible-option-default-bold:`true` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Create device"
      codeaffen.phpipam.device:
        username: "admin"
        password: "s3cr3t"
        server_url: "https://ipam.example.com"
        hostname: "leaf-example-01"
        ipaddress: "192.0.2.222"
        sections:
          - Example Inc.
          - DEVOPS department
        state: present

    - name: "Remove device"
      codeaffen.phpipam.device:
        username: "admin"
        password: "s3cr3t"
        server_url: "https://ipam.example.com"
        name: "leaf-example-001"
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

