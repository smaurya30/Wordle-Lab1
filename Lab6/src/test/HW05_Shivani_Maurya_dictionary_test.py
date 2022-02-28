import unittest
from python.HW03_Shivani_Maurya_dictionary import *
from unittest.mock import patch, mock_open
import os

class Test(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def testreadDictWords(self, mock_file):
        
        path = os.path.abspath("../../src/resources/words.txt")
        words = open(path, "r").read().split()
        mock_file.read_data = words
        assert readDictWords() == mock_file.read_data
        # mock_file.assert_called_with(path)
        
        
    @patch('builtins.input', side_effect=['aaaaa'])
    def testcheckIfWordExistInDict(self, mock_inputs):
        res = checkIfWordExistInDict('aaaaa')
        self.assertEqual(res, False)
        
        
    @patch('builtins.input', side_effect=['aaron'])
    def testcheckIfWordExistInDictTrue(self, mock_inputs):
        res = checkIfWordExistInDict('aaron')
        self.assertEqual(res, True)
        
        
    def testgetWord(self):
        res = getWord()
        # Word returned is not empty
        self.assertIsNot(res, "")
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        