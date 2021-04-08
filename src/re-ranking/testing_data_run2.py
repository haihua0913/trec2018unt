import json
import numpy as np
import pickle
import os.path

def document2vector(document, dictionary, leng):
    vec = np.zeros(leng)
    for word in document:
        if word in dictionary:
            ind = dictionary[word]
            vec[ind] += 1
    return list(vec)

dictionary = json.load(open("dictionary.json", "r"))
topics_raw = json.load(open("2018_clean_topic.json", "r"))
path_ab = "results/run2-expansion/abstracts_clean/topic"
path_pr = "results/run2-expansion/proceedings_clean/topic"
reg = pickle.load(open("regressor.pkl", "rb"))

topics = {}
for top in topics_raw['topics']:
    topics[int(top['topic_id'])-1] = top['clean_disease'] + top['clean_gene']
    
leng_dict = len(dictionary)
for top in range(50):
    
    documents_id = []
    documents_content = []
    
    print(top)
    topic_part = topics[top]
    topic_vec = document2vector(topic_part, dictionary, leng_dict)#part2
    
    if os.path.isfile(path_ab+"%d.json"%(top+1)):
        documents_ab = json.load(open(path_ab+"%d.json"%(top+1), "r"))
        for art in documents_ab['docs']:
            documents_id.append(art['doc_id'])
            document_vec = document2vector(art['clean_abstract'] + art['clean_title'], dictionary, leng_dict)
            documents_content.append(document_vec+topic_vec)
        
    if os.path.isfile(path_pr+"%d.json"%(top+1)):
        documents_pr = json.load(open(path_pr+"%d.json"%(top+1), "r"))
        for art in documents_pr['docs']:
            documents_id.append(art['doc_id'])
            document_vec = document2vector(art['clean_background'] + art['clean_title'], dictionary, leng_dict)
            documents_content.append(document_vec+topic_vec)      
        
    if not documents_content:
        continue  
        
    score_predict = reg.predict(documents_content)
        
    inds = np.argsort(-score_predict)
    retri = [documents_id[inds[i]] for i in range(len(documents_id))]
    
    json.dump(retri, open("results/run2-expansion/topic%d.json"%(top+1), "w"))