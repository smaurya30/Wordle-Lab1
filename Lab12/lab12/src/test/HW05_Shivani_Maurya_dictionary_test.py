import unittest
from unittest.mock import patch, mock_open
import os
import sys
from unittest.mock import MagicMock
magicMock = MagicMock()
sys.modules['HW_Shivani_Maurya_utility'] = magicMock
from python.HW03_Shivani_Maurya_dictionary import *

class Test(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def testreadDictWords(self, mock_file):
        d = Dictionary()
        path = os.path.abspath("../../src/resources/words.txt")
        words = open(path, "r").read().split()
        mock_file.read_data = words
        assert d.readDictWordsFive() == mock_file.read_data
        # mock_file.assert_called_with(path)
        
        
    @patch('builtins.input', side_effect=['aaaaa'])
    def testcheckIfWordExistInDict(self, mock_inputs):
        d = Dictionary()
        res = d.checkIfWordExistInDict('aaaaa')
        self.assertEqual(res, False)
        
        
    @patch('builtins.input', side_effect=['aaron'])
    def testcheckIfWordExistInDictTrue(self, mock_inputs):
        d = Dictionary()
        res = d.checkIfWordExistInDict('aaron')
        self.assertEqual(res, True)
        
        
    def testgetWord(self):
        d = Dictionary()
        res = d.getWord()
        # Word returned is not empty
        self.assertIsNot(res, "")
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        