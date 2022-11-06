import unittest
from translator import english_to_french,french_to_english
class frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")

class englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")        

unittest.main()        