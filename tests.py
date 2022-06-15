import unittest

from translator import english_to_french, english_to_german

class TestEnglish_To_French(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(""), "null") # test input is null
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test hello translates to bonjour.
        self.assertNotEqual(english_to_french('Good'), 'Mal')  # test when good doesnot translate to mal.

    
class TestEnglish_To_German(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_german(""), "null") # test input is null
        self.assertEqual(english_to_german('Hello'), 'Hallo')  # test hello translates to hallo.
        self.assertEqual(english_to_german('Honey'), 'Honig')  # test when honey translates to honig.

unittest.main()
