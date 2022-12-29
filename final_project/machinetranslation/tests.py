import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrech(unittest.TestCase): 

    def test_english_to_french_null(self):
        # If null input then translation = null
        self.assertIsNone(english_to_french(None),None)

    def test_english_to_french(self):
        # If 'Hello' input then translation = 'Bonjour'
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    
    def test_french_to_english__null(self):
        # If null input then translation = null
        self.assertIsNone(french_to_english(None),None)

    def test_french_to_english(self):
        # If 'Hello' input then translation = 'Bonjour'
        self.assertEqual(french_to_english('Bonjour'),'Hello')