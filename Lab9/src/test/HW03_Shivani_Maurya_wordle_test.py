import unittest, sys
from unittest.mock import patch, MagicMock
magicMock = MagicMock()
sys.modules['HW_Shivani_Maurya_utility'] = magicMock
from python.HW03_Shivani_Maurya_wordle import *
from unittest.mock import patch

class Test(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[['o','r','g','a','n'], ['o','c','c','u','r'], {'g','a','n'}, {'o','r'}])
    def testwordleFunc(self, mock_inputs):
        badWordSet = set()
        goodWordSet = set()
        w = Wordle(['o','r','g','a','n'], ['o','c','c','u','r'])
        resStr = w.wordleFunc(badWordSet, goodWordSet)
        self.assertEqual(resStr, (' `"""', {'g','a','n'}, {'o','r'}))
        
    @patch('builtins.input', side_effect=[['o','r','g','a','n'], ['o','c','c','u','r'], {'g','a','n'}, {'o','r'}])
    def testwordleFuncError(self, mock_inputs):
        badWordSet = set()
        goodWordSet = set()
        w = Wordle(['o','r','g','a','n'], ['o','c','c','u','r'])
        resStr = w.wordleFunc(badWordSet, goodWordSet)
        self.assertNotEqual(resStr, ('`````', {'g','a','n'}, {'o','r'}))
        
    @patch('builtins.input', side_effect=[[' ','`','"','"','"'], ['o','r','g','a','n'], ['o','c','c','u','r'],  {'g','a','n'}, {'o','r'}])
    def testwordHelper(self, mock_inputs):
        badWordSet = set()
        goodWordSet = set()
        w = Wordle(['o','r','g','a','n'], ['o','c','c','u','r'])
        w.result = [' ','`','"','"','"']
        resStr = w.wordHelper(badWordSet, goodWordSet)
        self.assertEqual(resStr, ({'g','a','n'}, {'o','r'}))

if __name__ == '__main__':
    unittest.main()