'''
Unit tests for English to French translator and French to English 
translator function in test.py
Name: Gabriel Ricardo Erazo
'''
import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    '''
    Test for null input and for the translation of the word 
    ‘Hello’ and ‘Bonjour’ for english_to_french
    '''
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour') #Test correct translation
        #self.assertEqual(english_to_french(''),'') #Test for null input   
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0),0)

class Testfrench_to_english(unittest.TestCase):
    '''
    Test for null input and for the translation of the word 
    ‘Bonjour’ and ‘Hello for french_to_english
    '''
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello') #Test correct translation
        #self.assertEqual(french_to_english(''),'') #Test for null input
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0),0)

unittest.main()
