
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.5.0

.. Anchors

.. _ansible_collections.codeaffen.phpipam.is_subnet_filter:

.. Anchors: short name for ansible.builtin

.. Title

codeaffen.phpipam.is_subnet filter -- Check if a subnet belongs to another
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This filter plugin is part of the `codeaffen.phpipam collection <https://galaxy.ansible.com/ui/repo/published/codeaffen/phpipam/>`_ (version 1.7.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install codeaffen.phpipam`.

    To use it in a playbook, specify: :code:`codeaffen.phpipam.is_subnet`.

.. version_added

.. rst-class:: ansible-version-added

New in codeaffen.phpipam 1.2.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- First argument is a subnet  second another. If the first subnet belongs to second


.. Aliases


.. Requirements





.. Input

Input
-----

This describes the input of the filter, the value before ``| codeaffen.phpipam.is_subnet``.

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
        <div class="ansibleOptionAnchor" id="parameter-_input"></div>

      .. _ansible_collections.codeaffen.phpipam.is_subnet_filter__parameter-_input:

      .. rst-class:: ansible-option-title

      **Input**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-_input" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Subnet in cidr format which should belongs to parent


      .. raw:: html

        </div>




.. Positional

Positional parameters
---------------------

This describes positional parameters of the filter. These are the values ``positional1``, ``positional2`` and so on in the following
example: ``input | codeaffen.phpipam.is_subnet(positional1, positional2, ...)``

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
        <div class="ansibleOptionAnchor" id="parameter-parent"></div>

      .. _ansible_collections.codeaffen.phpipam.is_subnet_filter__parameter-parent:

      .. rst-class:: ansible-option-title

      **parent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-parent" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Subnet where input should belongs to


      .. raw:: html

        </div>



.. Options


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
      192.0.2.0/25 | codeaffen.phpipam.is_subnet(192.0.2.0/24)




.. Facts


.. Return values

Return Value
------------

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
        <div class="ansibleOptionAnchor" id="return-_value"></div>

      .. _ansible_collections.codeaffen.phpipam.is_subnet_filter__return-_value:

      .. rst-class:: ansible-option-title

      **Return value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-_value" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      True if children belongs to parent and false if not or both networks are the same.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Christian Meißner


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

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

