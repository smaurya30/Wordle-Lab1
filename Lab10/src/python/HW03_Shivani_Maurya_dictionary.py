import os, sys 
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
class Dictionary():
    def __init__(self):
        self.wordSet = set()
        try:
            self.path = os.path.abspath("../../src/resources/")
            logging.basicConfig(filename=self.path+'/gameplay.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        except:
            print("Error:", sys.exc_info()[0], " in Gameplay Log, Dictionary module, occurred.".__str__())

    # picks a random wordle word
    # wordSet = set()
    def getWord(self):
        try: 
            words = self.readDictWordsFive()
            flag = 0
            
            
            if len(self.wordSet) == 1379:
                self.wordSet.clear()
            
            
            while(flag != 1):
                word_pos = random.randint(0, len(words)-1)
                if((words[word_pos] not in self.wordSet) and (len(words[word_pos]) != 0)):
                    flag=1
                    word = words[word_pos]
                    self.wordSet.add(word)
                    break
            
            logging.info("Wordle word set: "+str(self.wordSet).__str__())
            return word.lower()
        except:
            print("Error:", sys.exc_info()[0], " in getWord method, Dictionary module, occurred.".__str__())
        
    
    # reads the FiveLtterWord file
    def readDictWordsFive(self):
        try:
            u = utility.Utility()
            u.createFiveLetterWordsFile()
            # path = os.path.abspath("../../src/resources/FiveLtterWord.txt")
            words = open(self.path+"/FiveLtterWord.txt", "r").read().split()
            return words
        except:
            print("Error:", sys.exc_info()[0], " in readDictWordsFive, Dictionary module, occurred.".__str__())
    
    # check if the input word exists in the words file
    def checkIfWordExistInDict(self, inputWord):
        try:
            words = set(self.readDictWordsFive())
            if(inputWord in words):
                return True
            else:
                return False
        except:
            print("Error:", sys.exc_info()[0], " in checkIfWordExistInDict, Dictionary module, occurred.".__str__())
    
