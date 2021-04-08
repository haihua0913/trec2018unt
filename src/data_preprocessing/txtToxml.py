#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 2018/2/17
import os


def readTxt(filepath):
    files = os.listdir(filepath)
    for file in files:
        print(file)
        absolutepath = os.path.join(filepath, file)
        with open(absolutepath,'r+',encoding="utf8") as f:
            content = f.read()
            f.seek(0,0)
            f.write('<DOCS>\n'+content+'</DOCS>\n')


if __name__ == '__main__':
    readTxt('D:\\Academic_Study\\UNT_PHD\\projects\\TRECdata\\sample')