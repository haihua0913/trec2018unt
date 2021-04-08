#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 2018/5/26


import os
import sys
from lxml import etree
import xml.etree.ElementTree as ET
import xml.dom.minidom


def resultPaser(datapath):

    files = os.listdir(datapath)
    for file in files:
        print(file)
        filepath = os.path.join(datapath, file)
        print(filepath)
        text = open(filepath, encoding="utf-8").read()
        parser = etree.XMLParser(recover=True)
        root = ET.fromstring(text, parser=parser)
        print(root.tag)
        for child in root:
            if child.tag == 'DOC':
                for grandchild in child:
                    if grandchild.tag == 'DOCNO':
                        DOCID = grandchild.text
                        print(DOCID)
                    if grandchild.tag == 'TEXT':
                        for ggrandchild in grandchild:
                            if ggrandchild.tag == 'journal-title':
                                journaltitle = ggrandchild.text
                                print(journaltitle)
                            if ggrandchild.tag == 'article-title':
                                articletitle = ggrandchild.text
                                print(articletitle)
                            if ggrandchild.tag == 'abstract':
                                abstract = ggrandchild.text
                                print(abstract)
                            if ggrandchild.tag == 'ChemicalList':
                                ChemicalList = ggrandchild.text
                                print(ChemicalList)
                            if ggrandchild.tag == 'mesh-descriptors':
                                meshdescriptors = ggrandchild.text
                                print(meshdescriptors)
                            if ggrandchild.tag == 'mesh-qualifiers':
                                meshqualifiers = ggrandchild.text
                                print(meshqualifiers)
                        impl = xml.dom.minidom.getDOMImplementation()
                        dom = impl.createDocument(None, 'Document', None)
                        root = dom.documentElement

                        Doc_id = dom.createElement('Do_id')
                        Doc_text = dom.createTextNode(DOCID)
                        Doc_id.appendChild(Doc_text)
                        root.appendChild(Doc_id)

                        Journal = dom.createElement('Journal')
                        Journal_text = dom.createTextNode(str(journaltitle))
                        Journal.appendChild(Journal_text)
                        root.appendChild(Journal)

                        Doc_title = dom.createElement('Doc_title')
                        Doc_title_text = dom.createTextNode(str(articletitle))
                        Doc_title.appendChild(Doc_title_text)
                        root.appendChild(Doc_title)

                        Doc_abstract = dom.createElement('Doc_abstract')
                        Doc_abstract_text = dom.createTextNode(str(abstract))
                        Doc_abstract.appendChild(Doc_abstract_text)
                        root.appendChild(Doc_abstract)

                        Doc_ChemicalList = dom.createElement('Doc_ChemicalList')
                        Doc_ChemicalList_text = dom.createTextNode(str(ChemicalList))
                        Doc_ChemicalList.appendChild(Doc_ChemicalList_text)
                        root.appendChild(Doc_ChemicalList)

                        Doc_meshdescriptors = dom.createElement('Doc_meshdescriptors')
                        Doc_meshdescriptors_text = dom.createTextNode(str(meshdescriptors))
                        Doc_meshdescriptors.appendChild(Doc_meshdescriptors_text)
                        root.appendChild(Doc_meshdescriptors)

                        Doc_meshqualifiers = dom.createElement('Doc_meshqualifiers')
                        Doc_meshqualifiers_text = dom.createTextNode(str(meshqualifiers))
                        Doc_meshqualifiers.appendChild(Doc_meshqualifiers_text)
                        root.appendChild(Doc_meshqualifiers)

                        f = open('/home/haihua/TREC2017/Data_preprocess/All_abstracts/'+DOCID+'.xml', 'w', encoding='utf-8')
                        dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
                        f.close()


if __name__ == '__main__':
    resultPaser('/home/haihua/TREC2017/Original_Datacollection/Medline_Human')