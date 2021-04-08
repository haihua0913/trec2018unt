import json
import numpy as np
import metric
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import ShuffleSplit

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

result = []
rs = ShuffleSplit(n_splits=2, test_size=.25, random_state=0)
for layers in range(6,15,2):
    for train_index, test_index in rs.split(data):
        X_train = [data[ind] for ind in train_index]
        X_test = [data[ind] for ind in test_index]
        y_train = [label[ind] for ind in train_index]
        y_test = [label[ind] for ind in test_index]
        
        reg = MLPRegressor((layers,))
        reg.fit(X_train, y_train)
        
        y_predict = reg.predict(X_test)
        
        inds = np.argsort(-y_predict)
        retri = [y_test[inds[i]] for i in range(100)]
        
        p10 = metric.precision_at_k(retri, 10)
        rp = metric.r_precision(retri)
        infncdg = metric.ndcg_at_k(retri, len(retri), method=0)
        
        result.append([layers, p10, rp, infncdg])
        
json.dump(result, open("result.json", "w"))