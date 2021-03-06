#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.utils.xrange import xrange
from plugins.generic.syntax import Syntax as GenericSyntax

class Syntax(GenericSyntax):
    @staticmethod
    def escape(expression, quote=True):
        """
        >>> Syntax.escape("SELECT 'abcdefgh' FROM foobar")
        'SELECT CHAR(97)+CHAR(98)+CHAR(99)+CHAR(100)+CHAR(101)+CHAR(102)+CHAR(103)+CHAR(104) FROM foobar'
        """

        def escaper(value):
            return "+".join("%s(%d)" % ("CHAR" if ord(value[i]) < 256 else "NCHAR", ord(value[i])) for i in xrange(len(value)))

        return Syntax._escape(expression, quote, escaper)
