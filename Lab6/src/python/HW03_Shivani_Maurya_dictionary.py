import os 
import random
import HW_Shivani_Maurya_utility as utility
from _ast import Set
import logging

'''
Psuedocode:

1. Read the file from resources folder
2. put the dictionary wordws in a list
3. Pick a random word for Wordle Game

'''
path = os.path.abspath("../../src/resources/")
logging.basicConfig(filename=path+'/gameplay.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# picks a random wordle word
wordSet = set()
def getWord():
    words = readDictWordsFive()
    flag = 0
    
    
    if len(wordSet) == 1379:
        wordSet.clear()
    
    
    while(flag != 1):
        word_pos = random.randint(0, len(words)-1)
        if((words[word_pos] not in wordSet) and (len(words[word_pos]) != 0)):
            flag=1
            word = words[word_pos]
            wordSet.add(word)
            break
    
    logging.info("Wordle word set: "+str(wordSet))
    return word.lower()

# reads the FiveLtterWord file
def readDictWordsFive():
    utility.createFiveLetterWordsFile()
    path = os.path.abspath("../../src/resources/FiveLtterWord.txt")
    words = open(path, "r").read().split()
    print("Fiveletterword file len",len(words))
    return words

# check if the input word exists in the words file
def checkIfWordExistInDict(inputWord):
    words = set(readDictWordsFive())
    if(inputWord in words):
        return True
    else:
        return False

