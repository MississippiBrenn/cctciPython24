import unittest
from strings_ch1 import Chapter1

## to run $python3 -m unittest test_chapter1.py
class TestChapter1(unittest.TestCase):
    def setUp(self):
        self.chapter1 = Chapter1()
    def test_reverse_string(self):
        self.assertEqual(self.chapter1.reverseString('hello'), 'olleh')
        self.assertEqual(self.chapter1.reverseString('ho'), 'oh')
        self.assertEqual(self.chapter1.reverseString(''), '')
        if __name__ = '__main__': 
            unittest.main()
