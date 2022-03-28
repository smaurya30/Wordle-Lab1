import HW03_Shivani_Maurya_wordle as wordleModule
import HW03_Shivani_Maurya_dictionary as dictModule
import HW_Shivani_Maurya_statistics as statistics
import HW_Shivani_Maurya_utility as utility
from collections import Counter
import logging, os, sys
from fileinput import filename
from _stat import filemode
from Tools.scripts import google



class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None
        
    def __str__(self):
        return "%s" %(self.dataVal)
        
# class SLinkedList:
#     def __init__(self):
#         self.headVal = None
        
        
    
class UI():
    
    def __init__(self):
        self.d = dictModule.Dictionary()
        self.s = statistics.Statistics()
        self.u = utility.Utility()
        try:
            self.path = os.path.abspath("../../src/resources/")
            logging.basicConfig(filename=self.path+'/gameplay.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        except:
            print("Error:", sys.exc_info()[0], " in Gameplay Log, UI module, occurred.".__str__())
    '''
    Psuedocode:
    
    1. Get random word from dictionary module
    2. Get the guessed word from user input
    3. Validate the word and check if it exists in dictionary
    4. If all checks pass then send the word to wordle module to evaluate the letters in input word
    5. If the result is of length 0 then the word has been guessed
    6. Else user gets another 5 tries
    
    '''
    # def __str__(self):
        
    
    def checkWordle(self, setOfEnteredWords, word, wordleWordList, gamesPlayed, winCount, count, flag, Counter, badWordSet, goodWordSet):
        try:
            wordList = list(word)
            # Condition to check if word already exists in the set of entered word
            if (word in setOfEnteredWords):
                print("Word already entered".__str__())
                wordList = []
            # Condition to check if the length of the word is equal to 5
            elif (len(word.strip()) == 0):
                flag = -1
                gamesPlayed -= 1
            elif (len(wordList) != 5):
                print("Word length is not 5".__str__()) 
                wordList = []
            # condition to check if word does not contain any alphanumeric characters
            elif (word.isalpha() != True): 
                print("Word contains alphanumeric characters".__str__()) 
                wordList = []
            # condition checks if it is a dictionary word
            elif (self.d.checkIfWordExistInDict(word) == False):
                print("Not a dictionary word".__str__()) 
                wordList = []
            # increment the user attempt after updating the colors
            elif len(wordList) != 0:
                setOfEnteredWords.add(word)
                wm = wordleModule.Wordle(wordList, wordleWordList)
                result, badWordSet, goodWordSet = wm.wordleFunc(badWordSet, goodWordSet)
                # wm.wordleFunc()
                # result = wm.resultString
                if(len(result.strip()) == 0):
                    winCount += 1
                    Counter[str(count)] = Counter.get(str(count), 0) + 1
                    flag = 1
                    print("Result: ", result.__str__())
                    
                print(f'Attempt: {count} and Result: {result}'.__str__())
                count += 1
                
            return setOfEnteredWords, gamesPlayed, winCount, count, flag, Counter, badWordSet, goodWordSet
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in checkWordle method, UI Module, occurred.".__str__())
    
    
    def wordleUi(self, wordleWord, flag, winCount, Counter, gamesPlayed):
        try:
            count = 1;
            setOfEnteredWords = set();
            
            print("Top 50 most likely words")
            wordRankFile = self.u.readWordRankFile()
            x = slice(50)
            wordRankFile = wordRankFile[x]
            curr = dummy = Node(0)
            for rankWord in wordRankFile[x]:
                if rankWord != '':
                    e = rankWord.split(',')
                    curr.nextVal = Node(e[1])
                    print(curr.nextVal, end=", ")
                    curr = curr.nextVal
            print("-----------------------------")
            
            badWordSet = set()
            goodWordSet = set()
                
            while count < 7:
                wordleWordList = list(wordleWord)
                print("Enter a 5 letter word".__str__())
                word = input().lower()
                logging.info("Input word: "+word)
                setOfEnteredWords, gamesPlayed, winCount, count, flag, Counter, badWordSet, goodWordSet = self.checkWordle(setOfEnteredWords, word, wordleWordList, gamesPlayed, winCount, count, flag, Counter, badWordSet, goodWordSet)
                if flag == -1:
                    print("Word was: ", wordleWord.__str__())
                    break
                elif flag == 1:
                    break
                
            
            if flag == 1:
                flag = 0
                print("Word guessed".__str__())
                logging.info("Word guessed")
            elif flag == 0:
                print("Word was: ", wordleWord.__str__())
                print("Attempts exhausted".__str__())
                logging.info("Attempts exhausted")
                
            return flag, winCount, Counter, gamesPlayed
        except:
            print("Error:", sys.exc_info()[0], " in wordleUi method, UI Module occurred.".__str__())
    
            
    def statsFuncs(self):
        try:
            self.u.createFiveLetterWordsFile()
            letterFreqDictRes = self.s.letterFreq()
            convertLetterFreqDictRes = self.s.convertListToTuple(letterFreqDictRes.copy())
            print('Convert dictionary of lists into a dictionary of tuples - 2: ',convertLetterFreqDictRes.__str__())
            print('Dictionary of lists: ',letterFreqDictRes.__str__())
            freqDictTupleParseRes = self.s.writeTupleDictInFile()
            print('Parse the statistics file into a dictionary of tuples - 3: ',freqDictTupleParseRes.__str__())
            wordRankRes = self.s.wordRank(letterFreqDictRes)
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in statsFuncs, UI module, occurred.")
        
        
    def main(self):
        try:
            print()
            flag = 0
            gamesPlayed = 0
            winCount = 0
            Counter = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
            while(flag != -1):
                gamesPlayed += 1
                # wordleWord = dictModule.getWord()
                wordleWord = self.d.getWord()
                logging.info("Wordle word: "+wordleWord)
                # print(wordleWord)
                flag, winCount, Counter, gamesPlayed = self.wordleUi(wordleWord, flag, winCount, Counter, gamesPlayed)
                
                print("Game played: ", gamesPlayed.__str__())
                logging.info("Games Played: "+str(gamesPlayed))
                if gamesPlayed > 0:
                    winPerc = (winCount / gamesPlayed) * 100
                    print("Win Percentage: ", winPerc.__str__())
                    logging.info("Win Percent: "+str(winPerc))
                else:
                    winPerc = 0
                    print("Win Percentage: ", winPerc.__str__())
                    logging.info("Win Percent: "+str(winPerc))
                    
                print("Win count: ", winCount.__str__())
                logging.info("Win count: "+str(winCount))
                print("Guess Distribution: ", Counter.__str__())
                logging.info("Counter: "+str(Counter))
                
            # self.statsFuncs()
            print("Exited game".__str__())
            logging.info("Exited game")
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in main, UI Module, occurred.".__str__())
        

# main()
if __name__ == '__main__':
    ui = UI()
    ui.statsFuncs()
    ui.main()
    

# if __name__ == '__main__':
#     main()

