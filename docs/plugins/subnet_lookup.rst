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

.. Anchors

.. _ansible_collections.codeaffen.phpipam.subnet_lookup:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

codeaffen.phpipam.subnet -- lookup for subnet information
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `codeaffen.phpipam collection <https://galaxy.ansible.com/codeaffen/phpipam>`_ (version 1.5.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install codeaffen.phpipam`.

    To use it in a playbook, specify: :code:`codeaffen.phpipam.subnet`.

.. version_added

.. versionadded:: 1.5.0 of codeaffen.phpipam

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This lookup returns information about a subnet.


.. Aliases


.. Requirements


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                            <th>Configuration</th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-_terms"></div>
                    <b>_terms</b>
                    <a class="ansibleOptionLink" href="#parameter-_terms" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Subnet in CIDR notation</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-app_id"></div>
                    <b>app_id</b>
                    <a class="ansibleOptionLink" href="#parameter-app_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [phpipam]<br>app_id = None
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:PHPIPAM_APPID
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Application ID</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [phpipam]<br>password = None
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:PHPIPAM_PASSWORD
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Password to authenticate with the server</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-url"></div>
                    <b>url</b>
                    <a class="ansibleOptionLink" href="#parameter-url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [phpipam]<br>url = None
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:PHPIPAM_URL
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>URL of the server to query</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [phpipam]<br>username = None
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:PHPIPAM_USERNAME
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Username to authenticate with the server</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-verify_ssl"></div>
                    <b>verify_ssl</b>
                    <a class="ansibleOptionLink" href="#parameter-verify_ssl" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [phpipam]<br>verify_ssl = yes
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:PHPIPAM_VERIFY_SSL
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Whether to verify SSL certificates</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Attributes


.. Notes

Notes
-----

.. note::
   - This lookup requires the ipaddress module.
   - This lookup returns a list of ip addresses.

.. Seealso


.. Examples



.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Christian Meißner (@cmeissner)



.. Parsing errors

