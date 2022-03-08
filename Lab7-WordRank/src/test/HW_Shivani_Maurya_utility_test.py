import unittest
from unittest.mock import patch, mock_open
import os
import sys
from python.HW_Shivani_Maurya_utility import *

class Test(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def testreadDictWords(self, mock_file):
        
        path = os.path.abspath("../../src/resources/words.txt")
        words = open(path, "r").read().split()
        mock_file.read_data = words
        assert readDictWords() == mock_file.read_data
        # mock_file.assert_called_with(path)
        
        
    def testcreateFiveLetterWordsFile(self):
        createFiveLetterWordsFile()
        path = os.path.abspath("../../src/resources/FiveLtterWord.txt")
        words = open(path, "r").read().split()
        
        self.assertEqual(len(words), 1379)
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        