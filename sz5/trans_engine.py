# -*- coding: utf-8 -*-

"""
Base class for Translating service.

Such as DeepL.com and Google Translate will inherit this.
"""

__author__ = "5shangzhi"
__copyright__ = "Copyright 2022, 5shangzhi"
__credits__ = ["5shangzhi"]
__license__ = "MIT"
__version__ = "0.0.1"

import json
import os


def load_json_cfg(config):
    json_cfg = dict()
    if os.path.isfile(config):
        with open(config, 'r') as f:
            json_cfg = json.load(f)
            f.close()
    else:
        print("Failed to load Json config file :", config)

    return json_cfg


class TransEngine:
    def __init__(self, config):
        self.json_cfg = load_json_cfg(config)

    def get_ready(self, webdriver):
        pass

    def do_translating(self, text):
        return ""
