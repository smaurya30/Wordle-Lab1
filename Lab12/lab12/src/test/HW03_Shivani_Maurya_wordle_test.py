import unittest, sys
from unittest.mock import patch, MagicMock
magicMock = MagicMock()
sys.modules['HW_Shivani_Maurya_utility'] = magicMock
from python.HW03_Shivani_Maurya_wordle import *
from unittest.mock import patch

class Test(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[['o','r','g','a','n'], ['o','c','c','u','r'], {'g','a','n'}, {'o':[0]}, {'r':[1]}])
    def testwordleFunc(self, mock_inputs):
        badWordSet = set()
        greenLetters = dict()
        yellowLetters = dict()
        w = Wordle(['o','r','g','a','n'], ['o','c','c','u','r'])
        resStr = w.wordleFunc(badWordSet, greenLetters, yellowLetters)
        self.assertEqual(resStr, (' `"""', {'g','a','n'}, {'o':[0]}, {'r':[1]}))
        
    @patch('builtins.input', side_effect=[['o','r','g','a','n'], ['o','c','c','u','r'], {'g','a','n'}, {'o':[0]}, {'r':[1]}])
    def testwordleFuncError(self, mock_inputs):
        badWordSet = set()
        greenLetters = dict()
        yellowLetters = dict()
        w = Wordle(['o','r','g','a','n'], ['o','c','c','u','r'])
        resStr = w.wordleFunc(badWordSet, greenLetters, yellowLetters)
        self.assertNotEqual(resStr, ('`````', {'g','a','n'}, {'o':[0]}, {'r':[1]}))
        
    @patch('builtins.input', side_effect=[[' ','`','"','"','"'], ['o','r','g','a','n'], ['o','c','c','u','r'],  {'g','a','n'}, {'o':[0]}, {'r':[1]}])
    def testwordHelper(self, mock_inputs):
        badWordSet = set()
        greenLetters = dict()
        yellowLetters = dict()
        w = Wordle(['o','r','g','a','n'], ['o','c','c','u','r'])
        w.result = [' ','`','"','"','"']
        resStr = w.wordHelper(badWordSet, greenLetters, yellowLetters)
        self.assertEqual(resStr, ({'g','a','n'}, {'o':[0]}, {'r':[1]}))

if __name__ == '__main__':
    unittest.main()