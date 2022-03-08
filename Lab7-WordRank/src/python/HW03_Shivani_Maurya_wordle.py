import sys
'''
Pseudocode:

1. Result is initialized to '"'
2. First we check if any of the letters in the same position exist
3. If they do then result at that index is udated to ' '
4. And Wordle word at that index is replaced with '1'
5. Then we check for other letters from input word that exist in wordle word
6. If they do then result is updated to '`'

'''


def wordleFunc(inputWordList, wordleWordList):
    try:
        result = ['"','"','"','"','"']
        
        k=0
        for inWord,outWord in zip(inputWordList, wordleWordList):
            if inWord == outWord:
                result[k] = ' '
                wordleWordList[k] = "1"
            k += 1
                
        
        for i in range(len(inputWordList)):
            if result[i] != ' ':
                for j in range(len(wordleWordList)):
                    # not using a counter, replacing the letter with number 1 in string type
                    if i==j and inputWordList[i] == wordleWordList[j]:
                        result[i] = ' '
                        wordleWordList[j] = "1"
                        break
                    elif i!=j and inputWordList[i] == wordleWordList[j]:
                        result[i] = '`'
                        wordleWordList[j] = "1"
                        break
        # print(result)
        resultString = ''.join(result)  
        return resultString
    except:
        print("Error:", sys.exc_info()[0], " in wordleFunc method, Wordle Module, occurred.")