#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Haihua on 2018/2/17
import os

import shutil


def eachtopic(filepath,dicpath):
    releventDoc = []
    fileopen = open(dicpath, encoding="utf-8")
    for line in fileopen:
        releventDoc.append(line.strip('\n'))
    # print(releventDoc)
    newrelevent = [releventDoc[i:i + 100] for i in range(0, len(releventDoc), 100)]
    base = '/home/haihua/TREC2017/5731data/'
    i = 1
    for j in range(30):
        file_name = base+str(i)
        os.mkdir(file_name)
        i = i+1
    files = os.listdir(filepath)
    for file in files:
        filename = file.strip('.xml')
        if filename in newrelevent[0]:
            # print(filename)
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/1')
        elif filename in newrelevent[1]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/2')
        elif filename in newrelevent[2]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/3')
        elif filename in newrelevent[3]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/4')
        elif filename in newrelevent[4]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/5')
        elif filename in newrelevent[5]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/6')
        elif filename in newrelevent[6]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/7')
        elif filename in newrelevent[7]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/8')
        elif filename in newrelevent[8]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/9')
        elif filename in newrelevent[9]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/10')
        elif filename in newrelevent[10]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/11')
        elif filename in newrelevent[11]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/12')
        elif filename in newrelevent[12]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/13')
        elif filename in newrelevent[13]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/14')
        elif filename in newrelevent[14]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/15')
        elif filename in newrelevent[15]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/16')
        elif filename in newrelevent[16]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/17')
        elif filename in newrelevent[17]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/18')
        elif filename in newrelevent[18]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/19')
        elif filename in newrelevent[19]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/20')
        elif filename in newrelevent[20]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/21')
        elif filename in newrelevent[21]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/22')
        elif filename in newrelevent[22]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/23')
        elif filename in newrelevent[23]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/24')
        elif filename in newrelevent[24]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/25')
        elif filename in newrelevent[25]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/26')
        elif filename in newrelevent[26]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/27')
        elif filename in newrelevent[27]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/28')
        elif filename in newrelevent[28]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/29')
        elif filename in newrelevent[29]:
            shutil.copy(filepath+'/'+filename+'.xml', '/home/haihua/TREC2017/5731data/30')


if __name__ == '__main__':
    eachtopic('/home/haihua/TREC2017/Result_all', '/home/haihua/TREC2017/5731data/DOC_ID.txt')