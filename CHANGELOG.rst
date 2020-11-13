===============================
codeaffen.phpipam Release Notes
===============================

.. contents:: Topics


v1.2.0
======

Minor Changes
-------------

- Add `is_subnet` filter
- Add filter documentation

v1.1.1
======

Bugfixes
--------

- Fix `validate_certs` is not used for api connection (https://github.com/codeaffen/phpipam-ansible-modules/issues/27)

v1.1.0
======

Bugfixes
--------

- Fixing `There is no `validate_certs` parameter in modules` bug (https://github.com/codeaffen/phpipam-ansible-modules/issues/25)

v1.0.0
======

Major Changes
-------------

- Adapt documentation to reflect the final requirements
- Running tests against the new version and do some changes to work as expected
- Switch to stable version of `phpypam` module

v0.5.0
======

New Modules
-----------

- codeaffen.phpipam.device - Manage devices
- codeaffen.phpipam.device_type - Manage device types

v0.4.0
======

New Modules
-----------

- codeaffen.phpipam.vrf - Manage virtual routers and forwarders

v0.3.0
======

New Modules
-----------

- codeaffen.phpipam.domain - Manage L2 routing domains
- codeaffen.phpipam.nameserver - Manage nameservers
- codeaffen.phpipam.vlan - Manage vlans

v0.2.0
======

New Modules
-----------

- codeaffen.phpipam.address - Manage addresses

v0.1.0
======
