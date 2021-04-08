#!/usr/bin/env python
# encoding: utf-8
'''
@author: haihua
@contact: haihua.chen@unt.edu
@file:retrieval.py
@time:  3:44 PM
@desc:

'''
import  urllib.request


def trec_retrieve():
    
    # connection = urllib.request.urlopen('http://www.python.org/')
    connection = urllib.request.urlopen('http://iia01.ci.unt.edu:8983/solr/trec2018/select?q=(Doc_abstract:%20%22lung%20cancer%22^4%20OR%20%22lung%20carcinoma%22%20OR%20%22small-cell%20lung%20carcinoma%22%20OR%20SCLC%20OR%20%22non-small-cell%20lung%20carcinoma%22%20OR%20NSCLC%20OR%20Doc_title:%22lung%20cancer%22^4%20OR%20%22lung%20carcinoma%22%20OR%20%22small-cell%20lung%20carcinoma%22%20OR%20SCLC%20OR%20%22non-small-cell%20lung%20carcinoma%22%20OR%20NSCLC)%20AND%20(Doc_abstract:%20ROS1^4%20OR%20%22ROS%22%20OR%20%22MCF3%22%20OR%20%22c-ros-1%22%20OR%20Doc_title:%20ROS1^4%20OR%20%22ROS%22%20OR%20%22MCF3%22%20OR%20%22c-ros-1%22)%20AND%20(Doc_abstract:%20%22treatment%22%20OR%20%22therapy%22%20OR%20%22Surgery%22%20OR%20%22Radiotherapy%22%20OR%20%22Chemotherapy%22%20OR%20%22Targeted%20therapy%22%20OR%20%22Bronchoscopy%22%20OR%20%22Palliative%20care%22)')
    # connection = urllib.request.urlopen('http://iia01.ci.unt.edu:8983/solr/trec2018/select?q=lung%20cancer')
    response = eval(connection.read())
    # print(response)
    print(response['response']['numFound'])
    print(response['response']['docs'])

if __name__ == '__main__':
    trec_retrieve()
