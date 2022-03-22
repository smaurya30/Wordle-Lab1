import unittest, sys
from unittest.mock import patch, MagicMock
magicMock = MagicMock()
sys.modules['HW03_Shivani_Maurya_wordle'] = magicMock
sys.modules['HW03_Shivani_Maurya_dictionary'] = magicMock
sys.modules['HW_Shivani_Maurya_utility'] = magicMock
sys.modules['HW_Shivani_Maurya_statistics'] = magicMock
from python.HW03_Shivani_Maurya_ui import *


class Test(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[[set(), 'organ', ['o','c','c','u','r'], 0,0,0,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}]])
    def testcheckWordle(self, mock_inputs):
        ui = UI()
        res = ui.checkWordle(set(), 'organ', ['o','c','c','u','r'], 1,0,1,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0})
        self.assertEqual(res,({'organ'}, 1, 1, 2, 1, {'1': 1, '2': 0, '3': 0, '4': 0, '5': 0, '6':0}))
        
    @patch('builtins.input', side_effect=[[set(), 'lake', ['o','c','c','u','r'], 0,0,0,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}]])
    def testcheckWordleLength(self, mock_inputs):
        ui = UI()
        res = ui.checkWordle(set(), 'lake', ['o','c','c','u','r'], 1,0,1,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0})
        self.assertEqual(res,(set(), 1, 0, 1, 0, {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}))
        
    
    @patch('builtins.input', side_effect=[[set(), 'lake', ['o','c','c','u','r'], 0,0,0,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}]])
    def testcheckWordleSet(self, mock_inputs):
        ui = UI()
        res = ui.checkWordle({'aaron'}, 'aaron', ['o','c','c','u','r'], 1,0,1,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0})
        self.assertEqual(res,({'aaron'}, 1, 0, 1, 0, {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}))
        
    @patch('builtins.input', side_effect=[[set(), 'lake', ['o','c','c','u','r'], 0,0,0,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}]])
    def testcheckWordleQuit(self, mock_inputs):
        ui = UI()
        res = ui.checkWordle({'aaron'}, '', ['o','c','c','u','r'], 1,0,1,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0})
        self.assertEqual(res,({'aaron'}, 0, 0, 1, -1, {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}))
        
    @patch('builtins.input', side_effect=[[set(), 'lake', ['o','c','c','u','r'], 0,0,0,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}]])
    def testcheckWordleNotAlpha(self, mock_inputs):
        ui = UI()
        res = ui.checkWordle({'aaron'}, '@1ron', ['o','c','c','u','r'], 1,0,1,0,{'1':0, '2':0, '3':0, '4':0, '5':0, '6':0})
        self.assertEqual(res,({'aaron'}, 1, 0, 1, 0, {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}))
        
        
        
if __name__ == '__main__':
    unittest.main()