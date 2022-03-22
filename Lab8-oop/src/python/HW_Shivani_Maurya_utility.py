import os, random, sys

class Utility():
    def __init__(self):
        self.path = os.path.abspath("../../src/resources/")
        
    # reads the words file
    def readDictWords(self):
        try:
            # path = os.path.abspath("../../src/resources/words.txt")
            words = open(self.path+"/words.txt", "r").read().split()
            return words
        except:
            print("Error:", sys.exc_info()[0], " in readDictWords, Utility module, occurred.".__str__())
        
    
    # 1380
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
            print("Error:", sys.exc_info()[0], " in createFiveLetterWordsFilemethod, Utility module, occurred.".__str__())
        # finally:        
        #     f.close()
        
    # createFiveLetterWordsFile()