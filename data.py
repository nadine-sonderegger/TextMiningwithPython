# -*- coding: utf-8 -*-
"""data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zv6MARGQcrBbLHyjPVVMZVnRWsRnVMpV
"""

import csv
import json
import pandas as pd

# !wget http: // deepyeti.ucsd.edu/jianmo/amazon/sample/meta_Computers.json.gz

data = []
with open('meta_Computers.json') as f:
    for l in f:
        data.append(json.loads(l.strip()))

# total length of list, this number equals total number of products
print('Total number of products:', len(data))

# first row of the list
print(data[0])

# convert list into pandas dataframe
df = pd.DataFrame.from_dict(data)

print(len(df))

# remove rows with unformatted title (i.e. some 'title' may still contain html style content)

df3 = df.fillna('')
df4 = df3[df3.title.str.contains('getTime')]  # unformatted rows
df5 = df3[~df3.title.str.contains('getTime')]  # filter those unformatted rows
print(len(df4))
print(len(df5))

# how those unformatted rows look like
df4.iloc[0]

df = pd.DataFrame(data, columns=['description', 'title', 'image', 'brand', 'rank', 'main_cat', 'date',
                                 'asin', 'feature', 'tech1', 'also_buy', 'price',
                                 'also_view', 'tech2', 'details', 'similar_item'])
df.to_csv('Amazon_v2.csv', index=False, sep=',')
