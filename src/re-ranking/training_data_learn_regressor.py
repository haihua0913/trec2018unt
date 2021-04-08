import json
import numpy as np
import pickle
from sklearn.neural_network import MLPRegressor

LAYERS = 10

def document2vector(document, dictionary, leng):
    vec = np.zeros(leng)
    for word in document:
        if word in dictionary:
            ind = dictionary[word]
            vec[ind] += 1
    return list(vec)

dictionary = json.load(open("dictionary.json", "r"))
scores_ref = json.load(open("relevant_document_name_all_topic.json", "r"))
articles = json.load(open("articles_train.json", "r"))
topics_raw = json.load(open("2017_clean_topic.json", "r"))

topics = {}
for top in topics_raw['topics']:
    topics[int(top['topic_id'])-1] = top['clean_disease'] + top['clean_gene']
    
leng_dict = len(dictionary)
data = []
label = []
for top in range(30):
    
    topic_part = topics[top]
    topic_vec = document2vector(topic_part, dictionary, leng_dict)#part2
    
    documents_names_list = scores_ref[top]
    
    score = 0#part3
    for doc_name in documents_names_list[0]:
        if doc_name not in articles:
            continue
        document_part = articles[doc_name]
        document_vec = document2vector(document_part, dictionary, leng_dict)#part1
        data.append(document_vec + topic_vec)
        label.append(score)
        
    score = 1#part3
    for doc_name in documents_names_list[1]:
        if doc_name not in articles:
            continue
        document_part = articles[doc_name]
        document_vec = document2vector(document_part, dictionary, leng_dict)#part1
        data.append(document_vec + topic_vec)
        label.append(score)
        
    score = 2#part3
    for doc_name in documents_names_list[2]:
        if doc_name not in articles:
            continue
        document_part = articles[doc_name]
        document_vec = document2vector(document_part, dictionary, leng_dict)#part1
        data.append(document_vec + topic_vec)
        label.append(score)

reg = MLPRegressor((LAYERS,))
reg.fit(data, label)

pickle.dump(reg, open("regressor.pkl", "wb"))