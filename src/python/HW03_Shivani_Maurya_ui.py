import HW03_Shivani_Maurya_wordle as wordleModule
import HW03_Shivani_Maurya_dictionary as dictModule

'''
Psuedocode:

1. Get random word from dictionary module
2. Get the guessed word from user input
3. Validate the word and check if it exists in dictionary
4. If all checks pass then send the word to wordle module to evaluate the letters in input word
5. If the result is of length 0 then the word has been guessed
6. Else user gets another 5 tries

'''
def wordleUi(wordleWord, flag):
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
                flag = 1
                print("Result: ",result)
                break
            print(f'Attempt: {count} and Result: {result}')
            # colorDict = {};
            count += 1
    
    
    if flag == 1:
        print("Word guessed")
    elif flag == 0:
        print("Word was: ", wordleWord)
        print("Attempts exhausted")
        
    return flag

        
def main():
    flag = 0
    while(flag != -1):
        wordleWord = dictModule.getWord()
        flag = wordleUi(wordleWord, flag)
        
    print("Exited game")
    
    
main()
    

