#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 2018/2/17
import os
import xml.dom.minidom


def proceedingParser(datapath):

    files = os.listdir(datapath)
    for file in files:
        filename = file.strip('.txt')
        # print(filename)
        resultopen = open(datapath+'/'+filename+'.txt', encoding="utf-8")
        document = []
        for line in resultopen:
            data = line.strip()
            if len(data)!=0:
                document.append(data)
        # print(document)
        if len(document)>=3:
            meeting = document[0].split(':')
            # print(meeting)
            title = document[1].split(':')
            # print(title)
            background = document[2].split(':')
            # print(background)
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

            f = open('/home/haihua/TREC2017/Data_preprocess/All_proceedings/' + filename + '.xml', 'w', encoding='utf-8')
            dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
            f.close()
        else:
            continue


if __name__ == '__main__':
    proceedingParser('/home/haihua/TREC2017/Original_Datacollection/additional_abstracts')