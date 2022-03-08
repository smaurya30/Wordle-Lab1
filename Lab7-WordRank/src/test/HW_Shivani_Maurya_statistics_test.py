import unittest
from unittest.mock import patch, mock_open
import os
import sys
from python.HW_Shivani_Maurya_statistics import *

class Test(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def testreadWordsFive(self, mock_file):
        
        path = os.path.abspath("../../src/resources/FiveLtterWord.txt")
        words = open(path, "r").read().split()
        mock_file.read_data = words
        assert readWordsFive() == mock_file.read_data
    
    
    def testconvertListToTuple(self):
        convertLetterFreqDict = {'a':[0.25, 0, 0.5, 0, 0], 'b':[0.25, 0, 0.5, 0, 0]}
        convertedTup = {'a':(0.25, 0, 0.5, 0, 0), 'b':(0.25, 0, 0.5, 0, 0)}
        assert convertListToTuple(convertLetterFreqDict) == convertedTup
        
    @patch("builtins.open", new_callable=mock_open)
    def testwriteTupleDictInFile(self, mock_file):
        path = os.path.abspath("../../src/resources/letterFrequency.csv")
        words = open(path, "r").read().split('\n')
        mock_file.read_data = words
        self.assertEqual(len(words), 1)
    
    # def testFiles(self):
    #     path = os.path.abspath("../../src/resources/")
    #     if os.path.exists(path+"/letterFrequency.csv") == True:
            # self.assert
        
    
        
        
if __name__ == '__main__':
    unittest.main()