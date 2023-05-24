import requests
# this will eventually be the word passed to the function instead of just this specific word used here
payload = {'keyword':'りんご'}
# response in .json format
r = requests.get('https://jisho.org/api/v1/search/words',params=payload)




print(r.text)