import os, random, sys
import HW_Shivani_Maurya_db as db

class Utility():
    def __init__(self):
        self.path = os.path.abspath("../../src/resources/")
        self.dataB = db.DB()
        
    # reads the words file
    def readDictWords(self):
        try:
            # path = os.path.abspath("../../src/resources/words.txt")
            words = open(self.path+"/words.txt", "r").read().split()
            return words
        except:
            # DB Entry
            self.dataB.insertError("Error:", sys.exc_info()[0], " in readDictWords method, Utility module, occurred.".__str__())
            print("Error:", sys.exc_info()[0], " in readDictWords, Utility module, occurred.".__str__())
            
    def readWordRankFile(self):
        try:
            # path = os.path.abspath("../../src/resources/words.txt")
            words = open(self.path+"/wordRank.csv", "r").read().split()
            return words
        except:
            # DB Entry
            self.dataB.insertError("Error:", sys.exc_info()[0], " in readWordRankFile method, Utility module, occurred.".__str__())
            print("Error:", sys.exc_info()[0], " in readWordRankFile, Utility module, occurred.".__str__())
        
    # Create file with 5 letter words
    def createFiveLetterWordsFile(self):
        try:
            words = self.readDictWords()
            # newPath = os.path.abspath("../../src/resources/")
            f = open(self.path+"/FiveLtterWord.txt", "w")
            # f = open("FiveLtterWord.txt", "w")
            for word in words:
                if len(word) == 5:
                    f.write(word)
                    f.write("\n")
            f.close()
        except:
            # DB Entry
            self.dataB.insertError("Error:", sys.exc_info()[0], " in createFiveLetterWordsFilemethod method, Utility module, occurred.".__str__())
            print("Error:", sys.exc_info()[0], " in createFiveLetterWordsFilemethod, Utility module, occurred.".__str__())
