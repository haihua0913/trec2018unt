#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 2018/5/27
import os


def mergeXML(datapath):
    fileopen = open("D:\\result.xml", "a", encoding='utf-16')
    files = os.listdir(datapath)
    for file in files:
        filepath = os.path.join(datapath, file)
        text = open(filepath, encoding="utf-16")
        for line in text:
            if line.startswith("<Filing"):
                print(line)
                fileopen.write(line)
            else:
                continue


if __name__ == '__main__':
    mergeXML("D:\\Lobbying")