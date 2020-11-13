Filters
=======

Filters are used to manipulate data if needed.

is_subnet
---------

This filter checks wether a given subnet belongs to the second one. It returns `true` if first subnet belongs to second and `false` if not or both subnets are the same.

.. code-block:: yaml

   192.0.2.0/25 | codeaffen.phpipam.is_subnet(192.0.2.0/24)
