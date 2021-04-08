#!/usr/bin/env python
# encoding: utf-8
'''
@author: haihua
@contact: haihua.chen@unt.edu
@file:result_preprocess_proceeding.py
@time:  3:29 PM
@desc:

'''

import json
import os
import nltk


def result_preprocess(resultspath):
    # define sign and stop words
    sign = ["!", ",", ".", ":", ";", "'", "#", "$", "%", "&", "(", ")", "*", "[", "]", "?", "@", "_", "/", "{", "|",
            "}", "~", "--"]
    f_stopword = open("/home/iialab/TREC2018/stopwords.txt")
    stopwords = f_stopword.readlines()
    stop_sign = []
    for stopword in stopwords:
        stopword = stopword.strip("\n")
        stop_sign.append(stopword)
    
    # 解析json文件
    files = os.listdir(resultspath)
    keys = ["clean_background", "clean_title", "doc_id"]
    for file in files:
        clean_docs = []
        topic_num = file.strip(".json")
        filename = resultspath + "/" + file
        with open(filename, "r") as load_f:
            json_parsed = json.load(load_f)
            query = json_parsed["responseHeader"]["params"]["q"]
            numFound = json_parsed["response"]["numFound"]
            relevant_doc = json_parsed["response"]["docs"]
            # print(relevant_doc)
            for each_doc in relevant_doc:
                Background = each_doc["Background"]
                Doc_title = each_doc["Doc_title"]
                clean_background = []
                clean_title = []
                for c in sign:
                    Background = Background.replace(c, "").lower()
                    Doc_title = Doc_title.replace(c, "").lower()
                    sentence_background = nltk.word_tokenize(Background, language='english')
                    sentence_title = nltk.word_tokenize(Doc_title, language='english')
                for item in sentence_background:
                    if item in stop_sign:
                        continue
                    else:
                        clean_background.append(nltk.stem.SnowballStemmer('english').stem(item))
                # print(clean_abstract)
                
                for item in sentence_title:
                    if item in stop_sign:
                        continue
                    else:
                        clean_title.append(nltk.stem.SnowballStemmer('english').stem(item))
                # print(clean_title)
                
                Doc_id = each_doc["Doc_id"]
                dictionary = dict(zip(keys, [clean_background, clean_title, Doc_id]))
                clean_docs.append(dictionary)
        print(clean_docs)
        new_dic = dict(zip(["query", "numFound", "docs"], [query, numFound, clean_docs]))
        with open("/home/iialab/TREC2018/judge_result/run3-6topics/proceedings_clean/" + file,
                "w") as f:
            json.dump(new_dic, f)
            print("finish!")


if __name__ == '__main__':
    result_preprocess("/home/iialab/TREC2018/judge_result/run3-6topics/proceedings")