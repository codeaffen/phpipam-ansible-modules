#!/usr/bin/env python

import os

from plugins.module_utils.phpipam_helper import PhpipamAnsibleModule

if __name__ == "__main__":
    p = PhpipamAnsibleModule(server_url="https://devphpipam.meissner.sh")
    p.connect()
    sections = p.sections()
    print(sections)
