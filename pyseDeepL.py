#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A demo command line program to translate a txt file from English to Chinese
by using DeepL.com translating service.
"""

__author__ = "5shangzhi"
__copyright__ = "Copyright 2022, 5shangzhi"
__credits__ = ["5shangzhi"]
__license__ = "MIT"
__version__ = "0.0.1"

import argparse
import os.path

from sz5.chrome_browser import ChromeBrowser
from sz5.deepl_trans_engine import DeeplTransEngine


def parse_arguments():
    parser = argparse.ArgumentParser(description='translating an epub/txt book to the language what you want.')
    parser.add_argument('-f', '--from', help="epub/txt file to read (eg. en)", required=True)
    parser.add_argument('-o', '--to', help="specify the output file (eg. zh)", required=True)
    parser.add_argument('-c', '--conf', help="specify a json config file of the translating engine (eg. DeepL)", required=True)
    return vars(parser.parse_args())


def translate(config, txt_lines):
    deepl_eng = DeeplTransEngine(config)

    cb = ChromeBrowser(deepl_eng)
    cb.load_translating_page()
    dst_text = cb.do_translating(txt_lines)
    cb.close()

    return dst_text


if __name__ == "__main__":
    args = parse_arguments()
    txtfile = args['from']
    outfile = args['to']
    jsoncfg = args['conf']

    if not os.path.isfile(txtfile):
        print("Invalid file to read:", txtfile)
        exit(-1)
    if not os.path.isfile(jsoncfg):
        print("Invalid config file to read:", jsoncfg)
        exit(-1)

    res: str = ''
    with open(txtfile, 'r') as f:
        res = translate(jsoncfg, f.readlines())
        f.close()

    with open(outfile, 'w') as f:
        f.write(res)
        f.close()
