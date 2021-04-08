#!/usr/bin/env python
# encoding: utf-8
'''
@author: haihua
@contact: haihua.chen@unt.edu
@file:traning_data_process.py
@time:  12:21 PM
@desc:

'''
import json

from gensim import corpora
import os
from lxml import etree
import xml.etree.ElementTree as ET
import nltk

def train_data(datapath):
    # define sign and stop words
    sign = ["!", ",", ".", ":", ";", "'", "#", "$", "%", "&", "(", ")", "*", "[", "]", "?", "@", "_", "/", "{", "|",
            "}", "~", "--"]
    f_stopword = open("/home/iialab/TREC2018/stopwords.txt")
    stopwords = f_stopword.readlines()
    stop_sign = []
    for stopword in stopwords:
        stopword = stopword.strip("\n")
        stop_sign.append(stopword)

    # 解析xml文件
    files = os.listdir(datapath)
    keys = ["clean_background", "clean_title", "doc_id"]
    clean_docs = []
    for file in files:
        # print(file)
        Doc_id = file.strip(".xml")
        filepath = os.path.join(datapath, file)
        # print(filepath)
        parser = etree.XMLParser(recover=True)
        text = open(filepath, encoding="utf-8").read()
        root = ET.fromstring(text, parser=parser)
        # print(root.tag)
        clean_title = []
        clean_background = []
        for child in root:
            if child.tag == "Doc_title":
                title = child.text
                for c in sign:
                    title = title.replace(c, "").lower().strip("\n")
                    sentence = nltk.word_tokenize(title, language='english')
                # print(sentence)
                
                for item in sentence:
                    if item in stop_sign:
                        continue
                        # print(item)
                    else:
                        clean_title.append(nltk.stem.SnowballStemmer('english').stem(item))
                print(clean_title)
            
            elif child.tag == "Background":
                abstract = child.text
                for c in sign:
                    abstract = abstract.replace(c, "").lower().strip("\n")
                    sentence = nltk.word_tokenize(abstract, language='english')
                # print(sentence)
                
                for item in sentence:
                    if item in stop_sign:
                        continue
                        # print(item)
                    else:
                        clean_background.append(nltk.stem.SnowballStemmer('english').stem(item))
                print(clean_background)

        dictionary = dict(zip(keys, [clean_background, clean_title, Doc_id]))
        print(dictionary)
        clean_docs.append(dictionary)
    new_dic = dict(zip(["numFound", "docs"], [265, clean_docs]))
    print(new_dic)
    with open("/home/iialab/TREC2018/training_data_2017/train_proceedings.json", "w") as f:
        json.dump(new_dic, f)
        print("finish!")
            


if __name__ == '__main__':
    train_data("/home/iialab/TREC2018/training_data_2017/proceedings")