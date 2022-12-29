import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrech(unittest.TestCase): 

    def test_english_to_french_null(self):
        # If null input then translation = null
        self.assertIsNone(englishToFrench(None),None)

    def test_english_to_french(self):
        # If 'Hello' input then translation = 'Bonjour'
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    
    def test_french_to_english__null(self):
        # If null input then translation = null
        self.assertIsNone(frenchToEnglish(None),None)

    def test_french_to_english(self):
        # If 'Hello' input then translation = 'Bonjour'
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')