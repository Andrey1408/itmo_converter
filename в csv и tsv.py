import json
from pandas import json_normalize
# конвертация yaml в csv и tsv
with open(r'среда.json') as file:
    documents = json.load(file)
json_df = json_normalize(documents)
json_df.to_csv('xcsv.csv', index=False)
json_df.to_csv('xtsv.tsv', sep='\t', index=False)

