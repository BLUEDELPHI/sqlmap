#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.enums import HTTP_HEADER
from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "Secure Entry Server (United Security Providers)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, headers, code = get_page(get=vector)
        retval = code >= 400 and re.search(r"Secure Entry Server", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
        if retval:
            break

    return retval
