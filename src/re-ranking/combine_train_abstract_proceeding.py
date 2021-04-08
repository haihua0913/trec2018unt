import json

abstract = json.load(open("train_abstracts.json", "r"))
proceeding = json.load(open("train_proceedings.json", "r"))

articles = {}

for art in abstract['docs']:
    articles[art['doc_id']] = art['clean_abstract'] + art['clean_title']
    
for art in proceeding['docs']:
    articles[art['doc_id']] = art['clean_background'] + art['clean_title']
    
json.dump(articles,open("articles_train.json", "w"))