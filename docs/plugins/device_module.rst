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

.. _ansible_collections.codeaffen.phpipam.device_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

codeaffen.phpipam.device -- Manage devices
++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `codeaffen.phpipam collection <https://galaxy.ansible.com/codeaffen/phpipam>`_ (version 1.3.1).

    To install it use: :code:`ansible-galaxy collection install codeaffen.phpipam`.

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

Requirements
------------
The below requirements are needed on the host that executes this module.

- inflection
- ipaddress
- phpypam>=1.0.0


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
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
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"ansible"</div>
                                    </td>
                                                                <td>
                                            <div>API app name</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A descriptive text for that entity</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Hostname of the given device</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ipaddress"></div>
                    <b>ipaddress</b>
                    <a class="ansibleOptionLink" href="#parameter-ipaddress" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>IP address of the given device</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Password of the user to access phpIPAM server</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-rack"></div>
                    <b>rack</b>
                    <a class="ansibleOptionLink" href="#parameter-rack" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rack where the device belongs to.</div>
                                            <div>If set <em>starting_rack_unit</em> and <em>rack_units</em> are also required.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-rack_units"></div>
                    <b>rack_units</b>
                    <a class="ansibleOptionLink" href="#parameter-rack_units" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Size of device in <em>U</em>.</div>
                                            <div>If set <em>rack</em> and <em>starting_rack_unit</em> are also required.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sections"></div>
                    <b>sections</b>
                    <a class="ansibleOptionLink" href="#parameter-sections" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of sections where the device belongs to</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-server_url"></div>
                    <b>server_url</b>
                    <a class="ansibleOptionLink" href="#parameter-server_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>URL of the phpIPAM server</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_community"></div>
                    <b>snmp_community</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_community" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The SNMP community string</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_port"></div>
                    <b>snmp_port</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">161</div>
                                    </td>
                                                                <td>
                                            <div>The used SNMP port</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_queries"></div>
                    <b>snmp_queries</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_queries" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_timeout"></div>
                    <b>snmp_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The SNMP connection timeout</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_v3_auth_pass"></div>
                    <b>snmp_v3_auth_pass</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_v3_auth_pass" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The password to authenticate via SNMPv3</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_v3_auth_protocol"></div>
                    <b>snmp_v3_auth_protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_v3_auth_protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The used SNMPv3 auth protocol</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_v3_ctx_engine_id"></div>
                    <b>snmp_v3_ctx_engine_id</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_v3_ctx_engine_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>CTX engine id when using SNMPv3</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_v3_ctx_name"></div>
                    <b>snmp_v3_ctx_name</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_v3_ctx_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>CTX name when using SNMPv3</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_v3_priv_pass"></div>
                    <b>snmp_v3_priv_pass</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_v3_priv_pass" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The password to authenticate via SNMPv3 in privacy mode</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_v3_priv_protocol"></div>
                    <b>snmp_v3_priv_protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_v3_priv_protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The used SNMPv3 privacy protocol</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_v3_sec_level"></div>
                    <b>snmp_v3_sec_level</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_v3_sec_level" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The used SNMPv3 security level</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-snmp_version"></div>
                    <b>snmp_version</b>
                    <a class="ansibleOptionLink" href="#parameter-snmp_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The used SNMP version</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-starting_rack_unit"></div>
                    <b>starting_rack_unit</b>
                    <a class="ansibleOptionLink" href="#parameter-starting_rack_unit" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Which is the starting rack unit where the device is mounted.</div>
                                            <div>If set <em>rack</em> and <em>racK_units</em> are also required.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>State of the entity</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Device type of this device.</div>
                                            <div>The value has to reflect values from device types configured.</div>
                                            <div>Default device types are <em>Switch</em>, <em>Router</em>, <em>Firewall</em>, <em>Hub</em>, <em>Wireless</em>, <em>Database</em>, <em>Workstation</em>, <em>Laptop</em> and <em>Other</em>.</div>
                                            <div>User defined types can be created either via UI, API (e.g. <em>device_type</em> ansible module within this collection).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Username to access phpIPAM server</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
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
                                            <div>Is the TLS certificate of the phpIPAM server verified or not.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

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



.. Parsing errors

