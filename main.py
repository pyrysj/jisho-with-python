import csv 
from IPython.display import display
import os
import pandas as pd

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

# we do this for performance reasons 
dictionary = pd.concat(dfs, ignore_index=True)
# filtered = dictionary[dictionary[0].isin(keywords)]
filtered = dictionary.query("@dictionary[0] in @keywords")
display(filtered)   
