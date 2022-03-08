import os, sys
from string import ascii_lowercase


def readWordsFive():
    try:
        path = os.path.abspath("../../src/resources/FiveLtterWord.txt")
        words = open(path, "r").read().split()
        return words
    except:
        print("Error:", sys.exc_info()[0], " in readDictWordsFive, Dictionary module, occurred.")
        
        
def letterFreq():
    try:
        letterFreqDict = dict()
        ''' initializing dictionary ''' 
        for i in ascii_lowercase:
            letterFreqDict[i] = [0,0,0,0,0]
            
        words = readWordsFive()
        for word in words:
            wordLetters = list(word)
            for pos, letter in enumerate(wordLetters):
                l = letterFreqDict.get(letter)
                l[pos] = l[pos] + 1;
                letterFreqDict[letter] = l;
        
        noOfWords = len(words)
        for k,v in letterFreqDict.items():
            v = [ x/noOfWords for x in v ]
            letterFreqDict[k] = v
        
        path = os.path.abspath("../../src/resources/")
        f = open(path+"/letterFrequency.csv", "w")
        for k,v in letterFreqDict.items():
            f.write("%s,%s\n"%(k,v))
        f.close()
        return letterFreqDict
    except:
        print("Error:", sys.exc_info()[0], " in letterFreq, statistics module, occurred.")
        
        
def convertListToTuple(convertLetterFreqDict):
    try:
        for k,v in convertLetterFreqDict.items():
            vTup = tuple(v)
            convertLetterFreqDict[k] = vTup
        return convertLetterFreqDict
    except:
        print("Error:", sys.exc_info()[0], " in convertListToTuple, statistics module, occurred.")


def writeTupleDictInFile():
    try:
        freqDictTupleParse = dict()
        path = os.path.abspath("../../src/resources/letterFrequency.csv")
        stats = open(path, "r").read().split('\n')
        for stat in stats:
            if stat != '':
                listval = list(map(float, (stat[3:-2].split(','))))
                tupVal = tuple(listval)
                freqDictTupleParse[stat[0:1]] = tupVal
        return freqDictTupleParse
    except:
        print("Error:", sys.exc_info()[0], " in writeTupleDictInFile, statistics module, occurred.")

    
def wordRank(freqLetter):
    try:
        wordRanks = dict()
        # words = dictionary.readDictWordsFive()
        words = readWordsFive()
        for word in words:
            wordLetters = list(word)
            prodVal = 1
            for pos, letter in enumerate(wordLetters):
                l = freqLetter.get(letter)
                prodVal *= l[pos];
            wordRanks[word] = prodVal;
        
        sortedList = dict(sorted(wordRanks.items(), key=lambda x:x[1], reverse=True))
        path = os.path.abspath("../../src/resources/")
        f = open(path+"/wordRank.csv", "w")
        count = 1
        for k,v in sortedList.items():
            f.write("%s,%s,%s\n"%(count,k,v))
            count += 1
        f.close()
        
        return sortedList
    except:
        print("Error:", sys.exc_info()[0], " in wordRank, statistics module, occurred.")


      
# letterFreqDictRes = letterFreq()  
# convertLetterFreqDictRes = convertListToTuple(letterFreqDictRes.copy())
# print('Convert dictionary of lists into a dictionary of tuples - 2: ',convertLetterFreqDictRes)
# print('Dictionary of lists: ',letterFreqDictRes)
# freqDictTupleParseRes = writeTupleDictInFile()
# print('Parse the statistics file into a dictionary of tuples - 3: ',freqDictTupleParseRes)
# wordRankRes = wordRank(letterFreqDictRes)