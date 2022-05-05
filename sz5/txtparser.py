# -*- coding: utf-8 -*-

"""
A placeholder class here.

The read() function already implemented in baseclass Parser.
"""

__author__ = "5shangzhi"
__copyright__ = "Copyright 2022, 5shangzhi"
__credits__ = ["5shangzhi"]
__license__ = "MIT"
__version__ = "0.0.1"

from . import parser


class TxtParser(parser.Parser):

    def __init__(self, filename):
        super().__init__(filename)

    def __repr__(self):
        return f'TxtParser({self.filename})'
