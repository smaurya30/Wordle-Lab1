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
class Wordle():

    def __init__(self, inputWordList, wordleWordList):
        self.inputWordList = inputWordList
        self.wordleWordList = wordleWordList
        self.result = ['"','"','"','"','"']
        self.resultString = ""
        
    def __str__(self):
        return self
        
    # @property
    # def resultString(self):
    #     return self.resultString
    #
    # @resultString.setter
    # def resultString(self, val):
    #     self.resultString = val
    
    
    def wordleFunc(self):
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
            print(self.result.__str__())
            self.resultString = ''.join(self.result)  
            return self.resultString
        except:
            print("Error:", sys.exc_info()[0], " in wordleFunc method, Wordle Module, occurred.".__str__())