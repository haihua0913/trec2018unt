from xlrd import open_workbook
from xlutils.copy import copy
import json
import os


def judgement(resultspath):
    files = os.listdir(resultspath)
    for file in files:
        topic_num = file.strip(".json")
        filename = resultspath + "/" + file
        with open(filename, "r") as load_f:
            json_parsed = json.load(load_f)
            relevant_doc = json_parsed["response"]["docs"]
            # print(relevant_doc)
            rexcel = open_workbook('/home/iialab/TREC2018/judge_data.xlsx')
            rows = rexcel.sheets()[0].nrows
            excel = copy(rexcel)
            table = excel.get_sheet(0)
            row = rows
            for data in relevant_doc:
                table.write(row, 0, topic_num)
                table.write(row, 1, data["Doc_id"])
                table.write(row, 2, "")
                row += 1
            excel.save('/home/iialab/TREC2018/judge_data.xlsx')


if __name__ == "__main__":
    judgement("/home/iialab/Desktop/dictionary_and_retrieval_results/judgment")