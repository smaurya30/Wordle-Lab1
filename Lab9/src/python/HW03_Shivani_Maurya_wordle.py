import sys
import HW_Shivani_Maurya_utility as utility
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
        return "%s" %(self.dataVal)
        
        
        
class Wordle():

    def __init__(self, inputWordList, wordleWordList):
        self.inputWordList = inputWordList
        self.wordleWordList = wordleWordList
        self.result = ['"','"','"','"','"']
        self.resultString = ""
        self.u = utility.Utility()
        
    def __str__(self):
        return self
    
    
    def wordHelper(self, badWordSet, goodWordSet):
        try:
            hintWords = set()
        
            for resWord, helperWord in zip(self.result, self.inputWordList):
                if resWord == ' ' or resWord == '`' :
                    # if helperWord in badWordSet:
                    badWordSet.discard(helperWord)
                    goodWordSet.add(helperWord)
                elif resWord == '"' and helperWord not in goodWordSet:
                    badWordSet.add(helperWord)
        
            fiveLetterWords = self.u.readWordRankFile()
        
            for fiveLetWordRank in fiveLetterWords:
                fiveLetWord = fiveLetWordRank.split(',')
                fiveLetWord = fiveLetWord[1]
                goodCount = 0
                badCount = 0
                for letter in goodWordSet:
                    if letter in fiveLetWord:
                        goodCount += 1
        
                for letter in badWordSet:
                    if letter not in fiveLetWord:
                        badCount += 1
        
                if (goodCount + badCount) == (len(goodWordSet) + len(badWordSet)):
                    hintWords.add(fiveLetWord)
        
            print("bad letters: ",badWordSet)
            print("good letters: ", goodWordSet)
            print("helper words")
            print(set(itertools.islice(hintWords, 50)))
        
            return badWordSet, goodWordSet
        except:
            print("Error:", sys.exc_info()[0], " in wordHelper method, Wordle Module, occurred.".__str__())
            
            
            
    # def wordHelper(self, badWordSet, goodWordSet):
    #     try:
    #         hintWords = set()
    #
    #         for resWord, helperWord in zip(self.result, self.inputWordList):
    #             if resWord == ' ' or resWord == '`' :
    #                 # if helperWord in badWordSet:
    #                 badWordSet.discard(helperWord)
    #                 goodWordSet.add(helperWord)
    #             elif resWord == '"' and helperWord not in goodWordSet:
    #                 badWordSet.add(helperWord)
    #
    #         fiveLetterWords = self.u.readWordRankFile()
    #         fiveLetWord = Node(0)
    #         for fiveLetWordRank in fiveLetterWords:
    #             ele = fiveLetWordRank.split(',')
    #
    #             fiveLetWord.nextVal = Node(ele[1])
    #             fiveLetWord = fiveLetWord.nextVal
    #             print("seq: ", fiveLetWord, end=", ")
    #             goodCount = 0
    #             badCount = 0
    #             for letter in goodWordSet:
    #                 if letter in fiveLetWord:
    #                     goodCount += 1
    #
    #             for letter in badWordSet:
    #                 if letter not in fiveLetWord:
    #                     badCount += 1
    #
    #             if (goodCount + badCount) == (len(goodWordSet) + len(badWordSet)):
    #                 hintWords.add(fiveLetWord)
    #
    #
    #         print("bad letters: ",badWordSet)
    #         print("good letters: ", goodWordSet)
    #         print("helper words")
    #         print(set(itertools.islice(hintWords, 50)))
    #
    #         return badWordSet, goodWordSet
    #     except:
    #         print(sys.exc_info())
    #         print("Error:", sys.exc_info()[0], " in wordHelper method, Wordle Module, occurred.".__str__())


    def wordleFunc(self, badWordSet, goodWordSet):
        try:
            # result = ['"','"','"','"','"']
            
            k=0
            for inWord,outWord in zip(self.inputWordList, self.wordleWordList):
                if inWord == outWord:
                    self.result[k] = ' '
                    self.wordleWordList[k] = "1"
                k += 1
                    
            
            for i in range(len(self.inputWordList)):
                if self.result[i] != ' ':
                    for j in range(len(self.wordleWordList)):
                        # not using a counter, replacing the letter with number 1 in string type
                        if i==j and self.inputWordList[i] == self.wordleWordList[j]:
                            self.result[i] = ' '
                            self.wordleWordList[j] = "1"
                            break
                        elif i!=j and self.inputWordList[i] == self.wordleWordList[j]:
                            self.result[i] = '`'
                            self.wordleWordList[j] = "1"
                            break
            badWordSet, goodWordSet = self.wordHelper(badWordSet, goodWordSet)
            print(self.result.__str__())
            self.resultString = ''.join(self.result)  
            return self.resultString, badWordSet, goodWordSet
        except:
            print("Error:", sys.exc_info()[0], " in wordleFunc method, Wordle Module, occurred.".__str__())