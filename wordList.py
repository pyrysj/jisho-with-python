import pandas as pd
import os
# outline for module

# first, read the file
# second, pick out the words from the file
# third, merge the words and provide the tags for if the word is a noun etc.
# fourth, compile all information in the third step, save to intermediate file. 

# we assume a fixed folder structure here, this might not generalise well.
def readDict(folder_name: str):
    dfs = []
    for file in os.listdir(folder_name):
        if file.startswith("term_bank"):
            data = pd.read_json(folder_name+file)
            dfs.append(data) 
    # we do the actual generation of the full df outside of the loop to save on resources.
    dictionary = pd.concat(dfs, ignore_index=True)
    return dictionary    

# a bit ott, this might work better in the previous code bit?
def pickWords(keywords: list, dictionary:pd.DataFrame):
    filtered = dictionary.query("@dictionary[0] in @keywords")
    return filtered

# assuming fixed format here as well
# can (probably) be rewritten to work in more general cases.
def mergeTerms(data:pd.DataFrame, idx:int):
    merged = data.groupby([0,1],as_index=False)[idx].apply(list)
    return merged

def generateFile():
    pass 