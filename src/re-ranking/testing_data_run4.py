import json
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import os.path

class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
              yield TaggedDocument(doc,[self.labels_list[idx]])

def document2vector(document, dictionary, leng):
    vec = np.zeros(leng)
    for word in document:
        if word in dictionary:
            ind = dictionary[word]
            vec[ind] += 1
    return list(vec)

topics_raw = json.load(open("2018_clean_topic.json", "r"))
path_ab = "results/run4-expansion-weight-unsupervise/abstracts_clean/topic"
path_pr = "results/run4-expansion-weight-unsupervise/proceedings_clean/topic"
query_label = ['query']

topics = {}
for top in topics_raw['topics']:
    topics[int(top['topic_id'])-1] = top['clean_disease'] + top['clean_gene']
    
for top in range(50):
    
    documents_id = []
    documents_content = []
    
    print(top)
    topic_part = topics[top]
    
    if os.path.isfile(path_ab+"%d.json"%(top+1)):
        documents_ab = json.load(open(path_ab+"%d.json"%(top+1), "r"))
        for art in documents_ab['docs']:
            documents_id.append(art['doc_id'])
            documents_content.append(art['clean_abstract'] + art['clean_title'])
        
    if os.path.isfile(path_pr+"%d.json"%(top+1)):
        documents_pr = json.load(open(path_pr+"%d.json"%(top+1), "r"))
        for art in documents_pr['docs']:
            documents_id.append(art['doc_id'])
            documents_content.append(art['clean_background'] + art['clean_title'])    
        
    if not documents_content:
        continue 
        
    corp = LabeledLineSentence(documents_content+[topic_part], documents_id+query_label) 
    model = Doc2Vec(corp, vector_size=20, window=6, min_count=3, workers=8)
    retrieved = model.docvecs.most_similar('query', topn=len(documents_id))
    
    retri = [retrieved[i][0] for i in range(len(retrieved))]
    
    json.dump(retri, open("results/run4-expansion-weight-unsupervise/topic%d.json"%(top+1), "w"))