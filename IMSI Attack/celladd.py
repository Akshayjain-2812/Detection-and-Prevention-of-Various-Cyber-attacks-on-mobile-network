#creating a csv file with location id and respective sum id
import pandas as pd
import csv
data = pd.read_csv("D:\downloads\cell_towers1.csv\cellsort1.csv")
a = data.iloc[:3,data.columns.get_indexer(['cell'])].sum()
print(a)
with open("add1.csv", mode='w') as a:
    df = csv.writer(a, delimiter=',')
    df.writerow(['location id', 'Cell id sum'])
    j=1
    for x in range(65535):
        total=0
        total=data.loc[data['area']==j,'cell'].sum()
        df.writerow([j, total,])
        j+=1
        print(total)
