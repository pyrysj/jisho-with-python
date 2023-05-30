import csv 
import wordList
import deckFile

if __name__ == "__main__":
    # load the desired words, this can probably be done in an interactive way at some point.
    # keywords = pd.read_csv("word_list.csv")

    with open('word_list.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    # Note that the format of the list is unweildy for our purposes, list in lists. 
    # This is not what works. We need to flatten it. Very doable for our use, might
    # not be in other cases. 
    keywords = [item for sublist in data for item in sublist]
    # pass to list generating function
    # we define a string here for the folder name
    folder_name = "jmdict_english/"
    # pass it to the function, returns a dict
    dictionary = wordList.readDict(folder_name)

    filtered = wordList.pickWords(keywords,dictionary)
    # sort the words based off the words, tiebreak with readings, select the column containing the definitions
    merged_words = wordList.mergeTerms(filtered, 5)

    # NB: DO NOT save here in between, the knowledge that col '5' is a list gets lost. 
    # Might not be the best implementation
    new_mw = deckFile.convertToImportForm(merged_words)

    # simplifying code by not using this data
    # the code could eventually be abstracted where this could be used, but right now I feel like that would be diminishing returns.
    #verb_type = wordList.mergeTerms(filtered, 3)
    #word_type = wordList.mergeTerms(filtered, 4)
    wordList.generateFile(new_mw)
    # save the resulting dataframe as a .csv file. We are doing this to have a better time understanding what 
    # exactly happens.
    # checking execution time of code, seems relatively feasible but there might be room for improvement. 
