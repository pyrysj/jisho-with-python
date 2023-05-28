import csv 
from IPython.display import display
import os
import pandas as pd
from datetime import datetime

# checking execution of program
t1 = datetime.now()

# load the desired words, this can probably be done in an interactive way at some point.
# keywords = pd.read_csv("word_list.csv")

with open('word_list.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Note that the format of the list is unweildy for our purposes, list in lists. 
# This is not what works. We need to flatten it. Very doable for our use, might
# not be in other cases. 
keywords = [item for sublist in data for item in sublist]

# basic implementation with pandas
# we are using a set location, with a fixed dictionary provided 
# not included in the actual repository due to potential copyright concerns. 
# we define a string here for the folder name, allows for more flexible inmplementation eventually
folder_name = "jmdict_english/"
dfs = []
for file in os.listdir(folder_name):
    if file.startswith("term_bank"):
        data = pd.read_json(folder_name+file)
        dfs.append(data)

# we do the actual creation of the full dictionary outsoide of the loop for performance reasons 
dictionary = pd.concat(dfs, ignore_index=True)
filtered = dictionary.query("@dictionary[0] in @keywords")
# sort the words based off the words, tiebreak with readings, select the column containing the definitions
merged_words = filtered.groupby([0,1],as_index=False)[5].apply(list)
# for generating the cards - store the card type
# some efficiency savings could be done here ofr sure 
verb_type = filtered.groupby([0,1],as_index=False)[3].apply(list)
word_type = filtered.groupby([0,1],as_index=False)[4].apply(list)

# save the resulting dataframe as a .csv file. We are doing this to have a better time understanding what 
# exactly happens.

word_type.to_csv('result.csv',encoding='utf-8-sig')
t2 = datetime.now()
# checking execution time of code, seems relatively feasible but there might be room for improvement. 
print(f"{t2-t1}s to exectue code") 
