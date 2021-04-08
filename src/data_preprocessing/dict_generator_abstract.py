#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 6/15/2018
import string

from gensim import corpora
import os
from lxml import etree
import xml.etree.ElementTree as ET
import nltk


def dic_constructor(datapath):

    # define sign and stop words
    sign = ["!", ",", ".", ":", ";", "'", "#", "$", "%", "&", "(", ")", "*", "[", "]", "?", "@", "_", "/", "{", "|",
            "}", "~", "--"]
    f_stopword = open("D:\\Applications\\Visualization\\RapidMiner\\stopwords.txt")
    stopwords = f_stopword.readlines()
    stop_sign = []
    for stopword in stopwords:
        stopword = stopword.strip("\n")
        stop_sign.append(stopword)

    # 解析xml文件
    files = os.listdir(datapath)
    text_cluster = []
    for file in files:
        print(file)
        filepath = os.path.join(datapath, file)
        # print(filepath)
        parser = etree.XMLParser(recover=True)
        text = open(filepath, encoding="utf-8").read()
        root = ET.fromstring(text, parser=parser)
        # print(root.tag)
        for child in root:
            if child.tag == "Doc_title":
                title = child.text
                for c in sign:
                    title = title.replace(c, "").lower().strip("\n")
                    sentence = nltk.word_tokenize(title, language='english')
                # print(sentence)
                clean_title = []
                for item in sentence:
                    if item in stop_sign:
                        continue
                        # print(item)
                    else:
                        clean_title.append(nltk.stem.SnowballStemmer('english').stem(item))
                print(clean_title)
                if len(clean_title)>1:
                    clean_title.pop()
                    text_cluster.append(clean_title)
                else:
                    continue

            elif child.tag == "Doc_abstract":
                abstract = child.text
                for c in sign:
                    abstract = abstract.replace(c, "").lower().strip("\n")
                    sentence = nltk.word_tokenize(abstract, language='english')
                # print(sentence)
                clean_abstract = []
                for item in sentence:
                    if item in stop_sign:
                        continue
                        print(item)
                    else:
                        clean_abstract.append(nltk.stem.SnowballStemmer('english').stem(item))
                print(clean_abstract)
                if len(clean_abstract)>1:
                    clean_abstract.pop()
                    text_cluster.append(clean_abstract)
                else:
                    continue

            elif child.tag == "Doc_ChemicalList":
                chemical= child.text
                for c in sign:
                    chemical = chemical.replace(c, "").lower().strip("\n")
                    sentence = nltk.word_tokenize(chemical, language='english')
                    print(sentence)
                clean_chemical = []
                for item in sentence:
                    if item in stop_sign:
                        continue
                        # print(item)
                    else:
                        clean_chemical.append(nltk.stem.SnowballStemmer('english').stem(item))
                print(clean_chemical)
                if len(clean_chemical)>1:
                    clean_chemical.pop()
                    text_cluster.append(clean_chemical)
                else:
                    continue

            elif child.tag == "Doc_meshdescriptors":
                mesh_term = child.text
                for c in sign:
                    mesh_term = mesh_term.replace(c, "").lower().strip("\n")
                    sentence = nltk.word_tokenize(mesh_term, language='english')
                    # print(sentence)
                clean_mesh_term = []
                for item in sentence:
                    if item in stop_sign:
                        continue
                        # print(item)
                    else:
                        clean_mesh_term.append(nltk.stem.SnowballStemmer('english').stem(item))
                print(clean_mesh_term)
                if len(clean_mesh_term)>1:
                    clean_mesh_term.pop()
                    text_cluster.append(clean_mesh_term)
                else:
                    continue

            elif child.tag == "Doc_meshqualifiers":
                mesh_qualifier = child.text
                for c in sign:
                    mesh_qualifier = mesh_qualifier.replace(c, "").lower().strip("\n")
                    sentence = nltk.word_tokenize(mesh_qualifier, language='english')
                    # print(sentence)
                clean_mesh_qualifier = []
                for item in sentence:
                    if item in stop_sign:
                        continue
                        # print(item)
                    else:
                        clean_mesh_qualifier.append(nltk.stem.SnowballStemmer('english').stem(item))
                print(clean_mesh_qualifier)
                if len(clean_mesh_qualifier)>1:
                    clean_mesh_qualifier.pop()
                    text_cluster.append(clean_mesh_qualifier)
                else:
                    continue


    dictionary = corpora.Dictionary(text_cluster)
    dictionary.filter_extremes(no_below=2)
    dictionary.save_as_text('E:\\save_as_abstracts_dict.dict', sort_by_word=True)
    print(dictionary)
    print(u"词典中有效词的个数：" + str(dictionary.num_pos))


if __name__ == '__main__':
    dic_constructor("J:\\All_abstracts")