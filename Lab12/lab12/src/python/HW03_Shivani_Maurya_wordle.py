import sys
import HW_Shivani_Maurya_utility as utility
import HW_Shivani_Maurya_db as db
import itertools
'''
Pseudocode:

1. Result is initialized to '"'
2. First we check if any of the letters in the same position exist
3. If they do then result at that index is udated to ' '
4. And Wordle word at that index is replaced with '1'
5. Then we check for other letters from input word that exist in wordle word
6. If they do then result is updated to '`'

'''


class Node:

    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None
        
    def __str__(self):
        return "%s" % (self.dataVal)
        
        
class Wordle():

    def __init__(self, inputWordList, wordleWordList):
        self.inputWordList = inputWordList
        self.wordleWordList = wordleWordList
        self.result = ['"', '"', '"', '"', '"']
        self.resultString = ""
        self.u = utility.Utility()
        self.dataB = db.DB()
        
    def __str__(self):
        return self
    
    def wordHelper(self, badWordSet, greenLetters, yellowLetters, setOfEnteredWords):
        try:
            # hintWords = set()
            hintWords = list()
        
            for idx, (resWord, helperWord) in enumerate(zip(self.result, self.inputWordList)):
                if resWord == ' ':
                    badWordSet.discard(helperWord)
                    if greenLetters.get(helperWord) is not None:
                        vals = greenLetters.get(helperWord)
                        if idx not in vals:
                            vals.append(idx)
                            greenLetters.update({helperWord: vals})
                    else:
                        vals = list()
                        vals.append(idx)
                        greenLetters.update({helperWord: vals})
                elif resWord == '`':
                    badWordSet.discard(helperWord)
                    if greenLetters.get(helperWord) is None or idx not in greenLetters.get(helperWord):
                        if yellowLetters.get(helperWord) is not None:
                            vals = yellowLetters.get(helperWord)
                            if idx not in vals:
                                vals.append(idx)
                                yellowLetters.update({helperWord: vals})
                        else:
                            vals = list()
                            vals.append(idx)
                            yellowLetters.update({helperWord: vals})
                elif resWord == '"' and yellowLetters.get(helperWord) is None and greenLetters.get(helperWord) is None: 
                    badWordSet.add(helperWord)
        
            fiveLetterWords = self.u.readWordRankFile()
        
            greenValCount = 0
            for idxListVal in greenLetters.values():
                greenValCount += len(idxListVal)
                
            for fiveLetWordRank in fiveLetterWords:
                fiveLet = fiveLetWordRank.split(',')
                fiveLetWord = list(fiveLet[1])
                goodCount = 0
                greenCount = 0
                badCount = 0
                for letter, idxList in greenLetters.items():
                    if letter in fiveLetWord:
                        for i in idxList:
                            if fiveLetWord[i] == letter:
                                greenCount += 1
        
                for letter, idxList in yellowLetters.items():
                    if letter in fiveLetWord and fiveLetWord.index(letter) not in idxList :
                        goodCount += 1
                for letter in badWordSet:
                    if letter not in fiveLetWord:
                        badCount += 1
        
                if (goodCount + badCount + greenCount) == (greenValCount + len(badWordSet) + len(yellowLetters)):
                    # hintWords.add(fiveLet[1])
                    hintWords.append(fiveLet[1])
        
            print("bad letters: ", badWordSet)
            print("green letters: ", greenLetters)
            print("yellow letters: ", yellowLetters)
            # print(set(itertools.islice(hintWords, 50)))
            print("Likely words")
            print(hintWords[:50:])
            
            nextWord = ''
            for i in range(len(hintWords)):
                print("hintwords ",hintWords[i])
                if hintWords[i] not in setOfEnteredWords:
                    nextWord = hintWords[i]
                    break
                i +=1
                
        
            return badWordSet, greenLetters, yellowLetters, setOfEnteredWords, nextWord
        except:
            # DB Entry
            self.dataB.insertError("Error:", sys.exc_info()[0], " in wordHelper method, Wordle module, occurred.".__str__())
            print("Error:", sys.exc_info()[0], " in wordHelper method, Wordle Module, occurred.".__str__())

    def wordleFunc(self, badWordSet, greenLetters, yellowLetters, setOfEnteredWords):
        try:
            # result = ['"','"','"','"','"']

            k = 0
            for inWord, outWord in zip(self.inputWordList, self.wordleWordList):
                if inWord == outWord:
                    self.result[k] = ' '
                    self.wordleWordList[k] = "1"
                k += 1
            
            for i in range(len(self.inputWordList)):
                if self.result[i] != ' ':
                    for j in range(len(self.wordleWordList)):
                        # not using a counter, replacing the letter with number 1 in string type
                        if i == j and self.inputWordList[i] == self.wordleWordList[j]:
                            self.result[i] = ' '
                            self.wordleWordList[j] = "1"
                            break
                        elif i != j and self.inputWordList[i] == self.wordleWordList[j]:
                            self.result[i] = '`'
                            self.wordleWordList[j] = "1"
                            break
            badWordSet, greenLetters, yellowLetters, setOfEnteredWords, nextWord = self.wordHelper(badWordSet, greenLetters, yellowLetters,setOfEnteredWords)
            print(self.result.__str__())
            self.resultString = ''.join(self.result)  
            return self.resultString, badWordSet, greenLetters, yellowLetters, setOfEnteredWords, nextWord
        except:
            # DB Entry
            self.dataB.insertError("Error: {error} in wordleFunc method, Wordle module, occurred.".format(error = sys.exc_info()[0]))
            print("Error:", sys.exc_info()[0], " in wordleFunc method, Wordle Module, occurred.".__str__())