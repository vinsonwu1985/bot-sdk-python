#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""
from dueros.card.BaseCard import BaseCard

class TextStructure(BaseCard):

    def __init__(self):
        super(TextStructure, self).__init__()

    def setType(self, type):
        if type:
            self.data['type'] = type

    def setText(self, text):
        if text:
            self.data['text'] = text

    pass


if __name__ == '__main__':
    pass