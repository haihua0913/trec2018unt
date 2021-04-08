#!/usr/bin/env python
# encoding: utf-8
'''
@author: haihua
@contact: haihua.chen@unt.edu
@file:result_to_trecformat.py
@time:  8:32 PM
@desc:

'''
import codecs
import json
import os
import random
import sys

sys.setrecursionlimit(6000)

resultlist = []

def generateRand(counter, COUNT):
    tempFloat = random.random()
    format = ("%.4f" % tempFloat)
    # print(format)
    if(counter<=COUNT):
        if (format not in resultlist):
            resultlist.append(format)
            counter+=1
        generateRand(counter, COUNT)
    resultlist.sort(reverse=True)
    return resultlist


def result_to_trecformat(resultspath):
    file_object = codecs.open("trec_format.txt","w","utf-8")
    # 解析json文件
    files = os.listdir(resultspath)
    for file in files:
        topic_num = file.strip(".json")
        filename = resultspath + "/" + file
        with open(filename, "r") as load_f:
            json_parsed = json.load(load_f)
            numFound = json_parsed["response"]["numFound"]
            COUNT = numFound
            generateRand(1, COUNT)
            resultlist[0]
            print(resultlist[0])
            relevant_doc = json_parsed["response"]["docs"]
            index = 1
            for each_doc in relevant_doc:
                Doc_id = each_doc["Do_id"]
                topic_num = topic_num
                Q0 = "Q0"
                ID = Doc_id
                Rank = index
                Score = resultlist[index-1]
                Run_NAMES = "UNTIIA_RUN3"
                item = str(topic_num)+"\t"+str(Q0)+"\t"+str(ID)+"\t"+str(Rank)+"\t"+str(Score)+"\t"+Run_NAMES+"\r\n"
                file_object.write(item)
                print(str(topic_num)+"\t"+str(Q0)+"\t"+str(ID)+"\t"+str(Rank)+"\t"+str(Score)+"\t"+Run_NAMES)
                index+=1
                
    file_object.close()
    

if __name__ == '__main__':
    result_to_trecformat("/home/iialab/TREC2018/judge_result/run3-6topics/abstracts")