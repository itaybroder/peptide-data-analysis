from tkinter import FALSE
import pandas as pd

#parse NetGlyc-1.0 output and add it to the main df.
df = pd.read_csv("yair.csv")

def parseNetglyc(file_path, df):
    glyc_dict = {}
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.split()
            glyc_dict[line[2]] = line[3]
    
    potential_list = []
    for pep in df["peptide"]:
        flag = False
        for key,value in glyc_dict.items():
            
            if key in pep:
                potential_list.append(value)
                flag = True
            
        if not flag:
            potential_list.append(0)
            
    

    df["Potential"] = potential_list
        


    return df

df  = parseNetglyc("netGlycResult.txt", df)
df.to_csv("Nahom.csv")
print(df.head())
