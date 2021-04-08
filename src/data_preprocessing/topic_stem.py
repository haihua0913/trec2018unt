#!/usr/bin/env python
# encoding: utf-8
'''
@author: haihua
@contact: haihua.chen@unt.edu
@file:topic_stem.py
@time: 10:40 PM
@desc:
'''
import json
from lxml import etree
import xml.etree.ElementTree as ET
import nltk


def auto_retrieve(datapath):
    f_stopword = open("/home/iialab/TREC2018/stopwords.txt")
    stopwords = f_stopword.readlines()
    stop_sign = []
    for stopword in stopwords:
        stopword = stopword.strip("\n")
        stop_sign.append(stopword)
        
    keys = ["topic_id", "clean_disease", "clean_gene","clean_demographic"]
    parser = etree.XMLParser(recover=True)
    text = open(datapath, encoding="utf-8").read()
    root = ET.fromstring(text, parser=parser)
    print(root.tag)
    clean_topic = []
    for child in root:
        if child.tag == "topic":
            topic_index = child.attrib.get('number')
            print(topic_index)
            clean_disease = []
            clean_gene = []
            clean_demographic = []
            for grandchild in child:
                if grandchild.tag == "disease":
                    disease = grandchild.text
                    # print(disease)
                    disease = disease.lower()
                    sentence_disease = nltk.word_tokenize(disease, language='english')
                    for item in sentence_disease:
                        if item in stop_sign:
                            continue
                        else:
                            clean_disease.append(nltk.stem.SnowballStemmer('english').stem(item))
                # print(clean_disease)
                
                if grandchild.tag == "gene":
                    gene = grandchild.text
                    # print(gene)
                    gene = gene.replace(',', "").lower()
                    sentence_gene = nltk.word_tokenize(gene, language='english')
                    for item in sentence_gene:
                        if item in stop_sign:
                            continue
                        else:
                            clean_gene.append(nltk.stem.SnowballStemmer('english').stem(item))
                # print(clean_gene)
                
                if grandchild.tag == "demographic":
                    demographic = grandchild.text
                    # print(demographic)
                    demographic = demographic.lower()
                    sentence_demographic = nltk.word_tokenize(demographic, language='english')
                    for item in sentence_demographic:
                        if item in stop_sign:
                            continue
                        else:
                            clean_demographic.append(nltk.stem.SnowballStemmer('english').stem(item))
                # print(clean_demographic)

            dictionary = dict(zip(keys, [topic_index, clean_disease, clean_gene, clean_demographic]))
            # print(dictionary)
            clean_topic.append(dictionary)
    print(clean_topic)
    new_dic = dict(zip(["total_topics", "topics"], [50, clean_topic]))
    with open("/home/iialab/TREC2018/2017_clean_topic.json", "w") as f:
        json.dump(new_dic, f)
        print("finish!")
    

if __name__ == '__main__':
    auto_retrieve("/home/iialab/TREC2018/2017-TREC-PM-Topics.xml")