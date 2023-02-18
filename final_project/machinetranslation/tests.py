'''
Unit tests for English to French translator and French to English 
translator function in test.py
Name: Gabriel Ricardo Erazo
'''
import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    '''
    Test for null input and for the translation of the word 
    ‘Hello’ and ‘Bonjour’ for englishToFrench
    '''
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour') #Test correct translation
        #self.assertEqual(englishToFrench(''),'') #Test for null input   
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0),0)

class TestFrenchToEnglish(unittest.TestCase):
    '''
    Test for null input and for the translation of the word 
    ‘Bonjour’ and ‘Hello for frenchToEnglish
    '''
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello') #Test correct translation
        #self.assertEqual(frenchToEnglish(''),'') #Test for null input
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        self.assertNotEqual(frenchToEnglish("None"), '')
        self.assertNotEqual(frenchToEnglish(0),0)

unittest.main()
