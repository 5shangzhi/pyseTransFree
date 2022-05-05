# -*- coding: utf-8 -*-

"""
Using Chrome webdriver(selenium) to do the translating work.
"""

__author__ = "5shangzhi"
__copyright__ = "Copyright 2022, 5shangzhi"
__credits__ = ["5shangzhi"]
__license__ = "MIT"
__version__ = "0.0.1"

from sz5.browser import Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class ChromeBrowser(Browser):
    def __init__(self, trans_engine):
        webdrv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        super(ChromeBrowser, self).__init__(webdriver=webdrv, trans_engine=trans_engine)

    def load_translating_page(self):
        return self.trans_engine.get_ready(self.webdriver)

    def do_translating(self, text) -> str:
        if type(text) is str:
            return self.trans_engine.do_translating_str(text)
        elif type(text) is list:
            return self.trans_engine.do_translating_list(text)
        else:
            print("not implemented!")
            return ""

