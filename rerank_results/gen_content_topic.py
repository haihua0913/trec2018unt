import json
import os

path = "results/"

for file in os.listdir(path):
    
    abstract_path = path + file + '/' + 'abstracts' + '/topic'
    proceeding_path = path + file + '/' + 'proceedings' + '/topic'
    rerank_path = path + file + '/' + 'rerank' + '/topic'
    out_path = path + file + '/' + 'rerank_topic_with_content' + '/topic'
    
    for top in range(50):
    
        abstract_list = []
        abstract_dict = {}
        proceeding_dict = {}
        rerank = []
        abstract = {}
        proceeding = []
        
        
        
        print(top)
        
        if os.path.isfile(rerank_path+"%d.json"%(top+1)):
            rerank = json.load(open(rerank_path+"%d.json"%(top+1), "r", encoding="utf8"))
            
        if os.path.isfile(abstract_path+"%d.json"%(top+1)):
            abstract = json.load(open(abstract_path+"%d.json"%(top+1), "r", encoding="utf8"))
        
            abstract = abstract['response']['docs']
            for ab in abstract:
                abstract_dict[ab['Do_id']] = {'Doc_abstract':       ab['Doc_abstract'], 
                                              'Doc_title':          ab['Doc_title'],
                                              'Journal':            ab['Journal'],
                                              'Doc_ChemicalList':   ab['Doc_ChemicalList'],
                                              'Doc_meshdescriptors':ab['Doc_meshdescriptors'],
                                              'Doc_meshqualifiers': ab['Doc_meshqualifiers']}
        
        
        
        if os.path.isfile(proceeding_path+"%d.json"%(top+1)):
            proceeding = json.load(open(proceeding_path+"%d.json"%(top+1), "r", encoding="utf8"))
        
            proceeding = proceeding['response']['docs']
            for pr in proceeding:
                proceeding_dict[pr['Doc_id']] = {'Meeting_name': pr['Meeting_name'], 
                                              'Background':     pr['Background'],
                                              'Doc_title':      pr['Doc_title']}
        
        if not rerank:
            continue 
        
        
        for doc in rerank:
            if doc in abstract_dict:
                abstract_list.append([doc, abstract_dict[doc]])
            else:
                abstract_list.append([doc, proceeding_dict[doc]])
                
        json.dump(abstract_list, open(out_path+"%d.json"%(top+1), "w"))