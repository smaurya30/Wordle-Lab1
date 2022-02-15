'''
@author: Shivani Maurya
'''

'''
Pseudocode:

1. Wordle word to be guessed is specified
2. Initialized 'count' that tracks user attempts and 'setOfEnteredWords' as a set
3. Take string input word from user and convert it to list
4. Check if the word hasn't already been entered, and validate the size and if its alphanumeric
5. Add word to the setOfEnteredWords 
6. Initialize color for all letters to gray
7. Loop over the wordle word and input word
8. If letter exists in the wordle word at a different position then change its color to yellow
9. If letter exists at the same position as wordle word then change color to green
10. If all letters are green then exit loop else goto step 3 and repeat 6 times

'''


wordleWord = ["s","o","n","a","r"]
count = 1;
setOfEnteredWords = set();
flag = 0
while count < 7:
    print("Enter a 5 letter word")
    word = input().lower()
    wordList = list(word)
    
    # Condition to check if word already exists in the set of entered word
    if(word in setOfEnteredWords):
        print("Word already entered")
        wordList = []
    # Condition to check if the length of the word is equal to 5
    elif (len(wordList) != 5):
        print("Word length is not 5") 
        wordList = []
    # condition to check if word does not contain any alphanumeric characters
    elif (word.isalpha() != True): 
        print("Word contains alphanumeric characters") 
        wordList = []
    # increment the user attempt after updating the colors
    else:
        setOfEnteredWords.add(word)
        colorDict = {wordList[i]: "gray" for i in range(0,len(wordList),1)}
        
        for i in range(len(wordList)):
            for j in range(len(wordleWord)):
                # Condition to check if entered word is at the same position as the wordle word
                if i==j and wordList[i] == wordleWord[j]:
                    colorDict[wordList[i]] = "green"
                    break
                # Consition to check if the entered letter exists anywhere in the wordle word
                elif i!=j and wordList[i] == wordleWord[j]:
                    colorDict[wordList[i]] = "yellow"
                    break
        # if all letters are green then exit loop
        if(all(val=="green" for val in colorDict.values())):
            flag = 1
            print("Result: ",colorDict)
            break
        print(f'Attempt: {count} and Result: {colorDict}')
        colorDict = {};
        count += 1
        
if flag == 1:
    print("Word guessed")
else:
    print("Attempts exhausted")