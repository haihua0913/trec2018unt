import codecs
import json
import os
import xlsxwriter

def judgement(resultspath):
    files = os.listdir(resultspath)
    print(files)
    for file in files:
        topic_num = file.strip(".json")
        filename = resultspath + "\\" + file
        i = 1
        with codecs.open(filename, "rb") as load_f:
            json_parsed = json.loads(load_f.read())
            relevant_doc = json_parsed["response"]["docs"]
            print(relevant_doc)
            workbook = xlsxwriter.Workbook('D:\\judge.xlsx')

            worksheet = workbook.add_worksheet("run1")
            for data in relevant_doc:
                print(data["Do_id"])
                worksheet.write(i,'1',topic_num)
                worksheet.write(i,'2',data["Do_id"])
                worksheet.write(i,'3',"")
                i += 1
    workbook.close()
        

if __name__=="__main__":
    judgement("E:\\dictionary_and_retrieval_results\\results\\run1\\abstracts")