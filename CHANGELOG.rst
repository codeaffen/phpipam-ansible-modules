===============================
codeaffen.phpipam Release Notes
===============================

.. contents:: Topics


v1.5.0
======

Bugfixes
--------

- fix `ModuleNotFoundError` while using the collection with ansible >= version 5

Minor Changes
-------------

- fix \#68 - add automatic testing facility for all modules
- fix \#69 - add facility to setup local phpipam environment
- fix \#70 - provide environment variable support for connection data

v1.4.0
======

Minor Changes
-------------

- Minor formatting and spelling fixes.
- Switch sphinx from recommonmark to myst_parser.

Bugfixes
--------

- fix \#57 - tag lookups failed when specified in an `address` task
- fix \#61 - Device type examples
- with [AHH538](https://issues.redhat.com/browse/AAH-538) `requires_ansible` is mandatory in `meta/runtime.yml`. So we add the minimum version for our collection here.

New Modules
-----------

- codeaffen.phpipam.location - Manage locations
- codeaffen.phpipam.tag - Manage tags

v1.3.1
======

Bugfixes
--------

- fix `KeyError 'section'` bug (https://github.com/codeaffen/phpipam-ansible-modules/issues/41)

v1.3.0
======

Bugfixes
--------

- Fixing `Creating same subnet in different sections isn't possible` bug (https://github.com/codeaffen/phpipam-ansible-modules/issues/33)

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
