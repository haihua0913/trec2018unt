#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 2018/5/24

import os
from lxml import etree
import xml.etree.ElementTree as ET

def resultPaser(datapath):
    alldoc = []
    files = os.listdir(datapath)
    for file in files:
        # print(file)
        filepath = os.path.join(datapath, file)
        # print(filepath)
        text = open(filepath, encoding="utf-8").read()
        parser = etree.XMLParser(recover=True)
        root = ET.fromstring(text, parser=parser)
        # print(root.tag)
        for child in root:
            if child.tag == 'DOC':
                for grandchild in child:
                    if grandchild.tag == 'DOCNO':
                        DOCID = grandchild.text
                        alldoc.append(DOCID)
        print(alldoc)
        print(len(alldoc))