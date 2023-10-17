
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.5.0

.. Anchors

.. _ansible_collections.codeaffen.phpipam.folder_module:

.. Anchors: short name for ansible.builtin

.. Title

codeaffen.phpipam.folder module -- Manage folders
+++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `codeaffen.phpipam collection <https://galaxy.ansible.com/ui/repo/published/codeaffen/phpipam/>`_ (version 1.7.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install codeaffen.phpipam`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.codeaffen.phpipam.folder_module_requirements>` for details.

    To use it in a playbook, specify: :code:`codeaffen.phpipam.folder`.

.. version_added

.. rst-class:: ansible-version-added

New in codeaffen.phpipam 1.7.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- create, update and delete folders


.. Aliases


.. Requirements

.. _ansible_collections.codeaffen.phpipam.folder_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- inflection
- ipaddress
- phpypam\>=1.0.0






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-app_id"></div>

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-app_id:

      .. rst-class:: ansible-option-title

      **app_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-app_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the folder to manage


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-parent"></div>

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-parent:

      .. rst-class:: ansible-option-title

      **parent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-parent" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of parent folder


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-permissions:

      .. rst-class:: ansible-option-title

      **permissions**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-permissions" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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
        <div class="ansibleOptionAnchor" id="parameter-section"></div>

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-section:

      .. rst-class:: ansible-option-title

      **section**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-section" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the section under which the folder is located


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-server_url"></div>

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-server_url:

      .. rst-class:: ansible-option-title

      **server_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-server_url" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of the entity


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-username:

      .. rst-class:: ansible-option-title

      **username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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

      .. _ansible_collections.codeaffen.phpipam.folder_module__parameter-validate_certs:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Is the TLS certificate of the phpIPAM server verified or not.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - This module needs a phpIPAM backend with version 1.4.1 or highter.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Create a folder"
      codeaffen.phpipam.folder:
        username: "admin"
        password: "s3cr3t"
        server_url: "https://ipam.example.com"
        name: "Example folder"
        section: "EXAMPLE INC"
        state: present

    - name: "Create a folder with parent"
      codeaffen.phpipam.folder:
        username: "admin"
        password: "s3cr3t"
        server_url: "https://ipam.example.com"
        folder: "Example sub folder"
        parent: "Example folder"
        section: "DEVOPS department"
        state: present




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-entity"></div>

      .. _ansible_collections.codeaffen.phpipam.folder_module__return-entity:

      .. rst-class:: ansible-option-title

      **entity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-entity" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

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
        <div class="ansibleOptionAnchor" id="return-entity/folders"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.codeaffen.phpipam.folder_module__return-entity/folders:

      .. rst-class:: ansible-option-title

      **folders**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-entity/folders" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of folders.


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


.. Parsing errors

