DOCUMENTATION = r'''
  name: is_subnet
  author: Christian Meißner
  version_added: '1.2.0'
  short_description: Check if a subnet belongs to another
  description:
    - First argument is a subnet  second another. If the first subnet belongs to second
  positional: _input, parent
  options:
    _input:
      description: Subnet in cidr format which should belongs to parent
      type: string
      required: true
    parent:
      description: Subnet where input should belongs to
      type: string
      required: true
'''

EXAMPLES = r'''
  192.0.2.0/25 | codeaffen.phpipam.is_subnet(192.0.2.0/24)
'''

RETURN = r'''
  _value:
    description: True if children belongs to parent and false if not or both networks are the same.
    type: bool
'''
