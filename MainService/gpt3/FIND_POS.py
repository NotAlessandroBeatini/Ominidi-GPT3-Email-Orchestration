
import pandas as pd
import re
import json
patternPO = r'(?<=PO\: )(.*?)(?=\n)'
pattern = r'(?<=Positions\: \[)(.*?)(?=\])'


def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

def conv(to_be_conv): #I pass a list containing strings
    conv = ""
    for x in to_be_conv: #each x is a string
        conv = conv + x + '-'
    if len(to_be_conv)==0:
        conv =r'alle'
    else:
        conv = conv[:-1]
    return conv



def get_pos(string_email):

    try:

        pre_json = []      #ora è per ogni riga, i.e. mail
        keys = []

        temp = string_email  #has to process this one
        all = re.findall('[0-9]+', temp)  #all the numbers
        ass_po = 0
        p = re.compile('[0-9]+')
        i = 0
        appoggio = []
        for m in p.finditer(temp):
            pos = m.group()

            if len(pos) == 1:  # potrebbero essere a due cifre
                if len(keys) == 0 or (ass_po != 0 and (m.start() - appoggio[-1].start()) >= 30):  # if there are no keys yet. or if the current pos is too far away from the other one
                    continue  # if it is too far, disregard

                pre_json.append((all[ass_po], pos))  # here couple key-pos es; [(10921,1),(10921,2)]

            elif (len(pos) == 10):
                ass_po = i
                keys.append(pos)  # here only keys
                appoggio.append(m)

            i = i + 1
                    #ora devo fare dictionary locale

        dict = {}
        for key in keys:
            list = []
            for x in pre_json:
                if x[0] == key:
                    list.append(x[1])
            converted = conv(list) #returns ['1-2'] fashion
            dict[key] = [converted]


        return (dict,keys)


    finally:
        pass

if __name__ == "__main__":
    path = r'C:\Users\Ale\Downloads\GPT-3-Hackaton-Dataset-handout.xlsx'
    df = pd.read_excel(path)
    string = df.iloc[0].loc["combined_email"]
    print(get_pos(string))
    print("fuck the police")
