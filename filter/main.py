# file = open('csv_recent.txt', 'r')
output = open('output.txt', 'a')

# input = file.read().splitlines()

# for line in input:
#     arr = line.split(',')
#     if len(arr) > 2:
#         output.write(arr[3] + '\n')


import pandas as pd

input_file = pd.read_csv('domainC2swithURLwithIP-30day-filter-abused.csv')

for index, row in input_file.iterrows():
    output.write(f"{row['domain']}\n")