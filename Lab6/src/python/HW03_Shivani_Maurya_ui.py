import HW03_Shivani_Maurya_wordle as wordleModule
import HW03_Shivani_Maurya_dictionary as dictModule
from collections import Counter
import logging, os
from fileinput import filename
from _stat import filemode


path = os.path.abspath("../../src/resources/")
logging.basicConfig(filename=path+'/gameplay.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

'''
Psuedocode:

1. Get random word from dictionary module
2. Get the guessed word from user input
3. Validate the word and check if it exists in dictionary
4. If all checks pass then send the word to wordle module to evaluate the letters in input word
5. If the result is of length 0 then the word has been guessed
6. Else user gets another 5 tries

'''


def checkWordle(setOfEnteredWords, word, wordleWordList, gamesPlayed, winCount, count, flag, Counter):
    wordList = list(word)
    # Condition to check if word already exists in the set of entered word
    if (word in setOfEnteredWords):
        print("Word already entered")
        wordList = []
    # Condition to check if the length of the word is equal to 5
    elif (len(word.strip()) == 0):
        flag = -1
        gamesPlayed -= 1
    elif (len(wordList) != 5):
        print("Word length is not 5") 
        wordList = []
    # condition to check if word does not contain any alphanumeric characters
    elif (word.isalpha() != True): 
        print("Word contains alphanumeric characters") 
        wordList = []
    # condition checks if it is a dictionary word
    elif (dictModule.checkIfWordExistInDict(word) == False):
        print("Not a dictionary word") 
        wordList = []
    # increment the user attempt after updating the colors
    elif len(wordList) != 0:
        setOfEnteredWords.add(word)
        result = wordleModule.wordleFunc(wordList, wordleWordList)
        if(len(result.strip()) == 0):
            winCount += 1
            Counter[str(count)] = Counter.get(str(count), 0) + 1
            flag = 1
            print("Result: ", result)
        print(f'Attempt: {count} and Result: {result}')
        count += 1
        
    return setOfEnteredWords, gamesPlayed, winCount, count, flag, Counter


def wordleUi(wordleWord, flag, winCount, Counter, gamesPlayed):
    count = 1;
    setOfEnteredWords = set();
    while count < 7:
        wordleWordList = list(wordleWord)
        print("Enter a 5 letter word")
        word = input().lower()
        logging.info("Input word: "+word)
        setOfEnteredWords, gamesPlayed, winCount, count, flag, Counter = checkWordle(setOfEnteredWords, word, wordleWordList, gamesPlayed, winCount, count, flag, Counter)
        if flag == -1:
            print("Word was: ", wordleWord)
            break
        elif flag == 1:
            break
        
    
    if flag == 1:
        flag = 0
        print("Word guessed")
        logging.info("Word guessed")
    elif flag == 0:
        print("Word was: ", wordleWord)
        print("Attempts exhausted")
        logging.info("Attempts exhausted")
        
    return flag, winCount, Counter, gamesPlayed

        
def main():
    flag = 0
    gamesPlayed = 0
    winCount = 0
    Counter = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
    while(flag != -1):
        gamesPlayed += 1
        wordleWord = dictModule.getWord()
        logging.info("Wordle word: "+wordleWord)
        # print(wordleWord)
        flag, winCount, Counter, gamesPlayed = wordleUi(wordleWord, flag, winCount, Counter, gamesPlayed)
        
        print("Game played: ", gamesPlayed)
        logging.info("Games Played: "+str(gamesPlayed))
        if gamesPlayed > 0:
            winPerc = (winCount / gamesPlayed) * 100
            print("Win Percentage: ", winPerc)
            logging.info("Win Percent: "+str(winPerc))
        else:
            winPerc = 0
            print("Win Percentage: ", winPerc)
            logging.info("Win Percent: "+str(winPerc))
            
        print("Win count: ", winCount)
        logging.info("Win count: "+str(winCount))
        print("Guess Distribution: ", Counter)
        logging.info("Counter: "+str(Counter))
        
    print("Exited game")
    logging.info("Exited game")
    

# main()

if __name__ == '__main__':
    main()

