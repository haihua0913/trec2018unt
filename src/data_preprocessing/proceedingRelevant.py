#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 2018/2/28
import os
import re
from lxml import etree
import xml.etree.ElementTree as ET
import xml.dom.minidom


def readRelevant(datapath,filepath):
    with open(filepath, encoding="utf-8") as f:
        releventDoc = []
        for fLine in f:
            fLine = fLine.strip('\n')
            line = re.split(r' ',fLine)
            if int(line[3]) == 2:
                releventDoc.append(line[2])
        print(releventDoc)
        files = os.listdir(datapath)
        for file in files:
            filename = file.strip('.txt')
            # print(filename)
            if filename in releventDoc:
                # print(filename)
                resultopen = open(datapath + '/' + filename + '.txt', encoding="utf-8")
                document = []
                for line in resultopen:
                    data = line.strip()
                    if len(data) != 0:
                        document.append(data)
                # print(document)
                meeting = document[0].split(':')
                print(meeting)
                title = document[1].split(':')
                print(title)
                background = document[2].split(':')
                print(background)
                impl = xml.dom.minidom.getDOMImplementation()
                dom = impl.createDocument(None, 'Document', None)
                root = dom.documentElement

                Meeting_name = dom.createElement('Meeting_name')
                Meeting_name_text = dom.createTextNode(title[1])
                Meeting_name.appendChild(Meeting_name_text)
                root.appendChild(Meeting_name)

                Doc_title = dom.createElement('Doc_title')
                Doc_title_text = dom.createTextNode(str(title[1]))
                Doc_title.appendChild(Doc_title_text)
                root.appendChild(Doc_title)

                Background = dom.createElement('Background')
                Background_text = dom.createTextNode(str(background))
                Background.appendChild(Background_text)
                root.appendChild(Background)

                f = open('/home/haihua/TREC2017/Results_proceeding_relevant/' + filename + '.xml', 'w',
                         encoding='utf-8')
                dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
                f.close()


if __name__ == '__main__':
    readRelevant("/home/haihua/TREC2017/Datacollection/additional_abstracts","/home/haihua/TREC2017/5731data/treceval-abstracts2017.txt")