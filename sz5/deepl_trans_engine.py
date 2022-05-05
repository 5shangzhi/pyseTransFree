# -*- coding: utf-8 -*-

"""
The business work here which using DeepL.com to translate it.

The working logic is according to the website page layout and elements.
It might be changed one day. So then you should change this file and the JSON config file.
"""

__author__ = "5shangzhi"
__copyright__ = "Copyright 2022, 5shangzhi"
__credits__ = ["5shangzhi"]
__license__ = "MIT"
__version__ = "0.0.1"

from sz5.trans_engine import TransEngine
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

MAX_CHARS = "max_chars"
URL = "url"
FROM = "from"
TO = "to"
SRC_CSS_CLASS = "src_textarea_class"
DST_CSS_CLASS = "dst_textarea_class"


class DeeplTransEngine(TransEngine):
    def __init__(self, config):
        super(DeeplTransEngine, self).__init__(config)

        self.url = self.build_deepl_trans_url()
        self.src_textarea_css = self.build_src_textarea_css()
        self.dst_textarea_css = self.build_dst_textarea_css()
        self.MAX_CHARS = self.json_cfg.get(MAX_CHARS)

        self.src_textarea = None
        self.dst_textarea = None

        self.prev_txt = ""
        self.cur_txt = ""

    def build_deepl_trans_url(self):
        d = self.json_cfg
        # url = https://www.deepl.com/translator#en/zh/
        return d.get(URL) + '#' + d.get(FROM) + '/' + d.get(TO) + '/'

    @staticmethod
    def _build_css_str(css_txt):
        return 'textarea.' + '.'.join(css_txt.split())

    # get sting: 'textarea.lmt__textarea.lmt__source_textarea.lmt__textarea_base_style'
    def build_src_textarea_css(self):
        return self._build_css_str(self.json_cfg.get(SRC_CSS_CLASS))

    # get string: 'textarea.lmt__textarea.lmt__target_textarea.lmt__textarea_base_style'
    def build_dst_textarea_css(self):
        return self._build_css_str(self.json_cfg.get(DST_CSS_CLASS))

    def get_ready(self, webdrv: webdriver):
        print("loading url:", self.url)
        webdrv.get(self.url)  # loading page: https://www.deepl.com/translator#en/zh/
        self.src_textarea = webdrv.find_element(by=By.CSS_SELECTOR, value=self.src_textarea_css)
        self.dst_textarea = webdrv.find_element(by=By.CSS_SELECTOR, value=self.dst_textarea_css)
        return True

    def get_trans_result(self):
        res = ''

        prev_txt = ''
        cur_txt = ''
        double_check = False
        while not prev_txt \
                or len(prev_txt) != len(cur_txt)\
                or not double_check:
            print("...")
            time.sleep(1)

            res = self.dst_textarea.get_property('value')
            if "[...]" not in res:
                if not prev_txt:
                    prev_txt = res
                else:
                    if cur_txt:
                        prev_txt = cur_txt
                    cur_txt = res

                if len(prev_txt) == len(cur_txt):  # we might get it.
                    # waiting more time(1s), and check again.
                    time.sleep(1)
                    res = self.dst_textarea.get_property('value')
                    prev_txt = cur_txt
                    cur_txt = res
                    double_check = True
                    print("double checked!")
        print("done!")
        return res

    def transit(self, txt):
        if len(txt) > 0:
            self.src_textarea.clear()
            self.src_textarea.send_keys(txt)
            return self.get_trans_result()
        return ''

    def do_translating_str(self, txt: str):
        return self.transit(txt)

    def do_translating_list(self, lines: list):
        # remove empty lines
        lines = list(filter(None, [l.strip() for l in lines]))

        line_nrs = [len(l) for l in lines]

        j = 0
        i = 0
        txt = ""
        count = 0
        res = ""
        while i < len(line_nrs):
            count = count + line_nrs[i]
            if count > self.MAX_CHARS:
                # current line should ignore, and will be counted in next loop
                if i > j:
                    txt = "\n\n".join(lines[j:i])
                    res = res + self.transit(txt)

                count = line_nrs[i]
                j = i

            if (i + 1) == len(line_nrs):  # reach the end
                txt = "\n\n".join(lines[j:(i + 1)])
                res = res + self.transit(txt)

            i = i + 1

        return res
