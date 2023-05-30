import csv 
from IPython.display import display
import os
import pandas as pd
from datetime import datetime
import wordList

# split the main file into two parts (to ease testing of the latter part)


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
# we define a string here for the folder name
folder_name = "jmdict_english/"
# pass it to the function, returns a dict
dictionary = wordList.readDict(folder_name)

filtered = wordList.pickWords(keywords,dictionary)
# sort the words based off the words, tiebreak with readings, select the column containing the definitions
merged_words = wordList.mergeTerms(filtered, 5)
wordList.generateFile(merged_words)

# simplifying code by not using this data
#verb_type = wordList.mergeTerms(filtered, 3)
#word_type = wordList.mergeTerms(filtered, 4)

# save the resulting dataframe as a .csv file. We are doing this to have a better time understanding what 
# exactly happens.
t2 = datetime.now()
# checking execution time of code, seems relatively feasible but there might be room for improvement. 
print(f"{t2-t1}s to exectue code") 
