import os, random, sys

# reads the words file
def readDictWords():
    try:
        path = os.path.abspath("../../src/resources/words.txt")
        words = open(path, "r").read().split()
        return words
    except:
        print("Error:", sys.exc_info()[0], " in readDictWords, Utility module, occurred.")
    

# 1380
# Create file with 5 letter words
def createFiveLetterWordsFile():
    try:
        words = readDictWords()
        newPath = os.path.abspath("../../src/resources/")
        f = open(newPath+"/FiveLtterWord.txt", "w")
        # f = open("FiveLtterWord.txt", "w")
        for word in words:
            if len(word) == 5:
                f.write(word)
                f.write("\n")
        f.close()
    except:
        print("Error:", sys.exc_info()[0], " in createFiveLetterWordsFilemethod, Utility module, occurred.")
    # finally:        
    #     f.close()
    
# createFiveLetterWordsFile()