#!/usr/bin/env python
# encoding: utf-8
'''
@author: haihua
@contact: haihua.chen@unt.edu
@file:trec-submission.py
@time:  4:12 PM
@desc:

'''

import codecs
import json
import os
import random
import re
import sys

sys.setrecursionlimit(6000)

resultlist = []


def generateRand(counter, COUNT):
    tempFloat = random.random()
    format = ("%.4f" % tempFloat)
    # print(format)
    if (counter <= COUNT):
        if (format not in resultlist):
            resultlist.append(format)
            counter += 1
        generateRand(counter, COUNT)
    resultlist.sort(reverse=True)
    return resultlist


def result_to_trecformat(resultspath):
    file_object = codecs.open("trec_format.txt", "w", "utf-8")
    # 解析json文件
    files = os.listdir(resultspath)
    files.sort()
    for file in files:
        # topic_num = file.strip(".json")
        topic_num = re.sub("\D","",file)
        filename = resultspath + "/" + file
        with open(filename, "r") as load_f:
            json_parsed = json.load(load_f)
            print(json_parsed)
            numFound = len(json_parsed)
            print("####################################"+str(numFound))
            COUNT = numFound
            generateRand(1, COUNT)
            resultlist[0]
            print(resultlist[0])
            index = 1
            for each_doc in json_parsed:
                Doc_id = each_doc
                topic_num = topic_num
                Q0 = "Q0"
                ID = Doc_id
                Rank = index
                Score = resultlist[index - 1]
                Run_NAMES = "UNTIIA_DGS"
                item = str(topic_num) + "\t" + str(Q0) + "\t" + str(ID) + "\t" + str(Rank) + "\t" + str(
                    Score) + "\t" + Run_NAMES + "\r\n"
                file_object.write(item)
                print(str(topic_num) + "\t" + str(Q0) + "\t" + str(ID) + "\t" + str(Rank) + "\t" + str(
                    Score) + "\t" + Run_NAMES)
                index += 1

    file_object.close()


if __name__ == '__main__':
    result_to_trecformat("/home/iialab/TREC2018/trec2018_results/run3")