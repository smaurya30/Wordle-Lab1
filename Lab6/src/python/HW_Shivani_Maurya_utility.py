import os, random

# reads the words file
def readDictWords():
    path = os.path.abspath("../../src/resources/words.txt")
    words = open(path, "r").read().split()
    return words


# 1380
# Create file with 5 letter words
def createFiveLetterWordsFile():
    words = readDictWords()
    newPath = os.path.abspath("../../src/resources/")
    f = open(newPath+"/FiveLtterWord.txt", "w")
    # f = open("FiveLtterWord.txt", "w")
    for word in words:
        if len(word) == 5:
            f.write(word)
            f.write("\n")
            
    f.close()
    
# createFiveLetterWordsFile()