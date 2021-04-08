import json

file = open("save_as_abstracts_dict.dict","r", encoding="utf8")
dict_abstract = file.readlines()
file.close



file = open("save_as_proceeding_dict.dict","r", encoding="utf8")
dict_proceeding = file.readlines()
file.close

dictionary = {}
cnt = 0

for term in dict_abstract:
    tok = term.split()[1]
    if not tok[0].isalpha():
        continue
    if int(term.split()[2]) < 3:
        continue
    if tok not in dictionary:
        dictionary[tok] = cnt
        cnt += 1


for term in dict_proceeding:
    tok = term.split()[1]
    if not tok[0].isalpha():
        continue
    if int(term.split()[2]) < 3:
        continue
    if tok not in dictionary:
        dictionary[tok] = cnt
        cnt += 1
        
json.dump(dictionary, open("dictionary.json", "w"))