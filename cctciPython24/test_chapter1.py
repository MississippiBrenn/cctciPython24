import unittest
from strings_ch1 import Chapter1

## to run $python3 -m unittest test_chapter1.py
class TestChapter1(unittest.TestCase):
    def setUp(self):
        self.chapter1 = Chapter1()
    
    def rotate_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        self.assertEqual(rotate90(matrix), expected)

    def test_string_compression(self):
        self.assertEqual(self.chapter1.stringCompression('mmmkkl'), 'm3k2l1')
        self.assertEqual(self.chapter1.stringCompression('a'), 'a1')
        self.assertEqual(self.chapter1.stringCompression(''), '')



    def test_one_away(self):
        self.assertEqual(self.chapter1.oneAway('talk', 'tak'), True)
        self.assertEqual(self.chapter1.oneAway('talk', 'talk'), True)
        self.assertEqual(self.chapter1.oneAway('taaak', 'talk'), False)

    def test_is_palindrome(self): 
        self.assertEqual(self.chapter1.palindromePermuation('taco cat'), True)
        self.assertEqual(self.chapter1.palindromePermuation('stars above'), False)

    def test_URLify(self): 
        self.assertEqual(self.chapter1.URLify('lazy dog'), 'lazy%20dog')
        self.assertEqual(self.chapter1.URLify('nospace'), 'nospace')
    def test_check_permutations(self):
        self.assertEqual(self.chapter1.checkPermutations('aba', 'aab'), True)
        self.assertEqual(self.chapter1.checkPermutations('aba', 'abb'), False)
        self.assertEqual(self.chapter1.checkPermutations('abcdef', 'aab'), False)
        
    def test_is_unique(self):
        self.assertEqual(self.chapter1.isUnique('aaaa'), False)
        self.assertEqual(self.chapter1.isUnique('abcd'),True)
        self.assertEqual(self.chapter1.isUnique('abcdd'),False)

    def test_reverse_string(self):
        self.assertEqual(self.chapter1.reverseString('hello'), 'olleh')
        self.assertEqual(self.chapter1.reverseString('ho'), 'oh')
        self.assertEqual(self.chapter1.reverseString(''), '')
    

   

        
        if __name__ == '__main__': 
            unittest.main()
