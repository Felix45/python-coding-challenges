from unittest import TestCase
from longest_palindrome import longest_palindrome

class LongestPalindromeTest(TestCase):
    def test_longest_palindrome_I(self):
      assert longest_palindrome('babad') == 'bab'

    def test_longest_palindrome_II(self):
      assert longest_palindrome('cbbd') == "bb"
