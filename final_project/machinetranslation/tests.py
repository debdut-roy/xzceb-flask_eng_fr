"""tests.py is to test the functions in translator.py"""
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrech(unittest.TestCase):
    """
    This class is to test various scenarios of english_to_french function
    """
    def test_english_to_french_null(self):
        """ If null input then translation = null"""
        self.assertIsNone(english_to_french(None),None)

    def test_english_to_french(self):
        """If 'Hello' input then translation = 'Bonjour'"""
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_english_to_french_empty(self):
        """If input is '' then translation = ''"""
        self.assertEqual(english_to_french(''),'')

    def test_english_to_french_random(self):
        """If 'Three' input then translation = 'Trois'"""
        self.assertEqual(english_to_french('Three'),'Trois')

class TestFrenchToEnglish(unittest.TestCase):
    """
    This class is to test various scenarios of french_to_english function
    """
    def test_french_to_english__null(self):
        """If null input then translation = null"""
        self.assertIsNone(french_to_english(None),None)

    def test_french_to_english(self):
        """If 'Hello' input then translation = 'Bonjour'"""
        self.assertEqual(french_to_english('Bonjour'),'Hello')

    def test_french_to_english__empty(self):
        """If input is '' then translation = ''"""
        self.assertEqual(french_to_english(''),'')

    def test_french_to_english_random(self):
        """If 'Je mange une pomme.' input then translation = 'I am eating an apple'"""
        self.assertEqual(french_to_english('Je mange une pomme.'),'I eat an apple.')

unittest.main()
