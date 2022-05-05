# -*- coding: utf-8 -*-

"""
The base class for browsers.

Chrome or FireFox (etc.) webdriver(selenium) is in its subclass.
"""

__author__ = "5shangzhi"
__copyright__ = "Copyright 2022, 5shangzhi"
__credits__ = ["5shangzhi"]
__license__ = "MIT"
__version__ = "0.0.1"

import json
import os.path


class Browser:

    def __init__(self, webdriver, trans_engine):
        self.webdriver = webdriver
        self.trans_engine = trans_engine

    def __repr__(self):
        return f'Browser({self.webdriver})'

    def close(self):
        self.webdriver.close()

    def load_translating_page(self):
        print("You need implement this in your sub class!")
        return False
