import pandas as pd
import csv

filename = './data/beauty/All_Beauty_5.json'
outfile = './csv/beauty4.csv'

with open(filename, 'r') as f:
    data = f.readlines()

data_json = "[" + ','.join(data) + ']'
data_df = pd.read_json(data_json)
data_df['reviewText'] = data_df['reviewText'].str.replace('\n', '')
data_df.to_csv(outfile, index=False, header=False, quotechar="'",quoting=csv.QUOTE_ALL)
