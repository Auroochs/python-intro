import unittest
from my_awesome_lib import text_processing

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(text_processing.count_words("Hello world"), 2)
        self.assertEqual(text_processing.count_words("To jest test."), 3)

    def test_reverse_text(self):
        self.assertEqual(text_processing.reverse_text("abc"), "cba")

    def test_is_palindrome(self):
        self.assertTrue(text_processing.is_palindrome("Anna"))
        self.assertFalse(text_processing.is_palindrome("Hello"))

if __name__ == '__main__':
    unittest.main()
