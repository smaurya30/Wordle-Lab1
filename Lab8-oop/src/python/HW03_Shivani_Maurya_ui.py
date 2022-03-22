import HW03_Shivani_Maurya_wordle as wordleModule
import HW03_Shivani_Maurya_dictionary as dictModule
import HW_Shivani_Maurya_statistics as statistics
from collections import Counter
import logging, os, sys
from fileinput import filename
from _stat import filemode

class UI():
    
    def __init__(self):
        self.d = dictModule.Dictionary()
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
        
    
    def checkWordle(self, setOfEnteredWords, word, wordleWordList, gamesPlayed, winCount, count, flag, Counter):
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
                result = wm.wordleFunc()
                # wm.wordleFunc()
                # result = wm.resultString
                if(len(result.strip()) == 0):
                    winCount += 1
                    Counter[str(count)] = Counter.get(str(count), 0) + 1
                    flag = 1
                    print("Result: ", result.__str__())
                print(f'Attempt: {count} and Result: {result}'.__str__())
                count += 1
                
            return setOfEnteredWords, gamesPlayed, winCount, count, flag, Counter
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in checkWordle method, UI Module, occurred.".__str__())
    
    
    def wordleUi(self, wordleWord, flag, winCount, Counter, gamesPlayed):
        try:
            count = 1;
            setOfEnteredWords = set();
            while count < 7:
                wordleWordList = list(wordleWord)
                print("Enter a 5 letter word".__str__())
                word = input().lower()
                logging.info("Input word: "+word)
                setOfEnteredWords, gamesPlayed, winCount, count, flag, Counter = self.checkWordle(setOfEnteredWords, word, wordleWordList, gamesPlayed, winCount, count, flag, Counter)
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
            s = statistics.Statistics()
            letterFreqDictRes = s.letterFreq()
            convertLetterFreqDictRes = s.convertListToTuple(letterFreqDictRes.copy())
            print('Convert dictionary of lists into a dictionary of tuples - 2: ',convertLetterFreqDictRes.__str__())
            print('Dictionary of lists: ',letterFreqDictRes.__str__())
            freqDictTupleParseRes = s.writeTupleDictInFile()
            print('Parse the statistics file into a dictionary of tuples - 3: ',freqDictTupleParseRes.__str__())
            wordRankRes = s.wordRank(letterFreqDictRes)
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in statsFuncs, Utility module, occurred.")
        
        
    def main(self):
        try:
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
                
            self.statsFuncs()
            print("Exited game".__str__())
            logging.info("Exited game")
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in main, UI Module, occurred.".__str__())
        

# main()
if __name__ == '__main__':
    ui = UI()
    ui.main()

# if __name__ == '__main__':
#     main()

