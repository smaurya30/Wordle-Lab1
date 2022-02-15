import HW03_Shivani_Maurya_wordle as wordleModule
import HW03_Shivani_Maurya_dictionary as dictModule
from collections import Counter

'''
Psuedocode:

1. Get random word from dictionary module
2. Get the guessed word from user input
3. Validate the word and check if it exists in dictionary
4. If all checks pass then send the word to wordle module to evaluate the letters in input word
5. If the result is of length 0 then the word has been guessed
6. Else user gets another 5 tries

'''

def wordleUi(wordleWord, flag, winCount, Counter, gamesPlayed):
    count = 1;
    setOfEnteredWords = set();
    while count < 7:
        wordleWordList = list(wordleWord)
        print("Enter a 5 letter word")
        word = input().lower()
        wordList = list(word)
        
        # Condition to check if word already exists in the set of entered word
        if (word in setOfEnteredWords):
            print("Word already entered")
            wordList = []
        # Condition to check if the length of the word is equal to 5
        elif (len(word.strip()) == 0):
            print("Word was: ", wordleWord)
            flag = -1
            gamesPlayed -= 1
            break
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
        else:
            setOfEnteredWords.add(word)
            result = wordleModule.wordleFunc(wordList, wordleWordList)
            if(len(result.strip()) == 0):
                winCount += 1
                Counter[str(count)] = Counter.get(str(count), 0) + 1
                flag = 1
                print("Result: ",result)
                break
            print(f'Attempt: {count} and Result: {result}')
            count += 1
    
    
    if flag == 1:
        print("Word guessed")
    elif flag == 0:
        print("Word was: ", wordleWord)
        print("Attempts exhausted")
        
    return flag, winCount, Counter, gamesPlayed

        
def main():
    flag = 0
    gamesPlayed = 0
    winCount = 0
    Counter = {'1':0, '2':0, '3':0, '4':0, '5':0}
    while(flag != -1):
        gamesPlayed += 1
        wordleWord = dictModule.getWord()
        print(wordleWord)
        flag, winCount, Counter, gamesPlayed = wordleUi(wordleWord, flag, winCount, Counter, gamesPlayed)
        
        print("Game played: ",gamesPlayed)
        winPerc = (winCount/gamesPlayed) * 100
        print("Win count: ", winCount)
        print("Win Percentage: ",winPerc)
        print("Guess Distribution: ",Counter)
        
    print("Exited game")
    
    
main()
    

