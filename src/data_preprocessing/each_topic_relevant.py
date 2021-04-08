#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 2018/2/28
import os
import re
import shutil

def each_topic_relevant(datapath,filepath):
    files = os.listdir(datapath)
    filelist = []
    for file in files:
        filename = file.strip('.xml')
        filelist.append(filename)
    print(filelist)
    with open(filepath, encoding="utf-8") as f:
        for fLine in f:
            fLine = fLine.strip('\n')
            line = re.split(r' ',fLine)
            if int(line[3]) == 2 and int(line[0]) == 1 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/1')
            elif int(line[3]) == 2 and int(line[0]) == 2 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/2')
            elif int(line[3]) == 2 and int(line[0]) == 3 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/3')
            elif int(line[3]) == 2 and int(line[0]) == 4 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/4')
            elif int(line[3]) == 2 and int(line[0]) == 5 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/5')
            elif int(line[3]) == 2 and int(line[0]) == 6 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/6')
            elif int(line[3]) == 2 and int(line[0]) == 7 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/7')
            elif int(line[3]) == 2 and int(line[0]) == 8 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/8')
            elif int(line[3]) == 2 and int(line[0]) == 9 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/9')
            elif int(line[3]) == 2 and int(line[0]) == 10 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/10')
            elif int(line[3]) == 2 and int(line[0]) == 11 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/11')
            elif int(line[3]) == 2 and int(line[0]) == 12 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/12')
            elif int(line[3]) == 2 and int(line[0]) == 13 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/13')
            elif int(line[3]) == 2 and int(line[0]) == 14 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/14')
            elif int(line[3]) == 2 and int(line[0]) == 15 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/15')
            elif int(line[3]) == 2 and int(line[0]) == 16 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/16')
            elif int(line[3]) == 2 and int(line[0]) == 17 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/17')
            elif int(line[3]) == 2 and int(line[0]) == 18 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/18')
            elif int(line[3]) == 2 and int(line[0]) == 19 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/19')
            elif int(line[3]) == 2 and int(line[0]) == 20 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/20')
            elif int(line[3]) == 2 and int(line[0]) == 21 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/21')
            elif int(line[3]) == 2 and int(line[0]) == 22 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/22')
            elif int(line[3]) == 2 and int(line[0]) == 23 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/23')
            elif int(line[3]) == 2 and int(line[0]) == 24 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/24')
            elif int(line[3]) == 2 and int(line[0]) == 25 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/25')
            elif int(line[3]) == 2 and int(line[0]) == 26 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/26')
            elif int(line[3]) == 2 and int(line[0]) == 27 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/27')
            elif int(line[3]) == 2 and int(line[0]) == 28 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/28')
            elif int(line[3]) == 2 and int(line[0]) == 29 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/29')
            elif int(line[3]) == 2 and int(line[0]) == 30 and line[2] in filelist:
                shutil.copy(datapath + '/' + line[2] + '.xml', '/home/haihua/TREC2017/5731data_relevant/30')

if __name__ == '__main__':
    each_topic_relevant("/home/haihua/TREC2017/Result_all_relevant", "/home/haihua/TREC2017/5731data/treceval-abstracts2017.txt")