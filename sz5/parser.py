# -*- coding: utf-8 -*-

"""
Base class for file parser.

A lot of file types should be implemented as subclass.
Such as TXT, EPUB, DOCX, MOBI, PDF...
"""

__author__ = "5shangzhi"
__copyright__ = "Copyright 2022, 5shangzhi"
__credits__ = ["5shangzhi"]
__license__ = "MIT"
__version__ = "0.0.1"

from os import path


class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.txt = ""

    def __repr__(self):
        return f'Parser({self.filename})'

    def read(self):
        if path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                self.txt = list(filter(None, [line.strip() for line in f.readlines()]))
                f.close()
        else:
            print("Failed to read. Get nothing!")

        return self.txt
