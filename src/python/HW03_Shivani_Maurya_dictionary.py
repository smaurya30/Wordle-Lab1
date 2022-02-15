import os 
import random

'''
Psuedocode:

1. Read the file from resources folder
2. put the dictionary wordws in a list
3. Pick a random word for Wordle Game

'''


# picks a random wordle word
def getWord():
    words = readDictWords()
    flag = 0
    while(flag != 1):
        word_pos = random.randint(0, len(words)-1)
        if(len(words[word_pos]) == 5):
            flag=1
            word = words[word_pos]
            break
    
    return word.lower()

# reads the words file
def readDictWords():
    path = os.path.abspath("../../src/resources/words.txt")
    words = open(path, "r").read().split()
    return words

# check if the input word exists in the words file
def checkIfWordExistInDict(inputWord):
    words = set(readDictWords())
    if(inputWord in words):
        return True
    else:
        return False

    
