import unittest

from translator import english_to_french

class TestEnglish_To_French(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(null), null) # test input is null
        self.assertEqual(english_to_french('hello'), 'bonjour')  # test hello translates to bonjour.
        self.assertNotEqual(english_to_french('good'), 'mal')  # test when good doesnot translate to mal.

    unittest.main()

from translator import english_to_german

class TestEnglish_To_German(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_german(null), null) # test input is null
        self.assertEqual(english_to_german('hello'), 'hallo')  # test hello translates to hallo.
        self.assertEqual(english_to_german('honey'), 'honig')  # test when honey translates to honig.

    unittest.main()
