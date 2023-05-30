# python-csv-to-anki

## Why
I was recently faced with a situation where I had to manually input a lot of words into the spaced repetition software Anki as there was no pre-existing deck avaliable for the material I was using. As one does, when faced with a repetitive problem, it can be resolved with code. I quickly coded this up as a quick summer side project. I found similar software, but wanted to regardless challenge myself in coding this script. There were numerous concerns (both personal and found online) with the similar software I found. Although it provided a workable end result, I was determined to push on with this poject.

## How
This is a (quick) script in Python for processing a .csv file containing (Japanese) expressions the user wants to batch convert into a format that can be used for the spaced repetition software Anki. The program receives an input file (right now hard-coded to a specific name, but easily modifiable) that is then converted to a list. The resulting list is then used to select the matching expressions and definitions from a separately provided folder containing dictionary files. (.json files) As with the input file, this is also hard-coded but could be easily altered.

## What next
Personally, I do not know. I more wanted to make this as a general proof of concept that this is doable with Python. I am sure there is a better way to do what I am doing, but I thought this would be an interesting project to pursue. There are a number of tweaks that one could do, for instance adding more customisation to the genration of the end file, adding more fields and other similar features. The use of other dictionaries than the one I used (JMDict) could be also considered. 

