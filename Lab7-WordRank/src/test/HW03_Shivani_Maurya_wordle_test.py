import unittest
from python.HW03_Shivani_Maurya_wordle import wordleFunc
from unittest.mock import patch

class Test(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[['o','r','g','a','n'], ['o','c','c','u','r']])
    def testwordleFunc(self, mock_inputs):
        resStr = wordleFunc(['o','r','g','a','n'], ['o','c','c','u','r'])
        self.assertEqual(resStr, ' `"""')
        
    @patch('builtins.input', side_effect=[['o','r','g','a','n'], ['o','c','c','u','r']])
    def testwordleFuncError(self, mock_inputs):
        resStr = wordleFunc(['o','r','g','a','n'], ['o','c','c','u','r'])
        self.assertNotEqual(resStr, '`````')
        

if __name__ == '__main__':
    unittest.main()