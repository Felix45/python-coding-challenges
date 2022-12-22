from unittest import TestCase
from reverse_vowels import reverse_vowels

class ReverseVowelsTest(TestCase):
    def test_reverse_vowels_hello(self):
      assert reverse_vowels("hello") == "holle"

    def test_reverse_vowels_leetcode(self):
      assert reverse_vowels("leetcode") == "leotcede"

    def test_reverse_vowels_aA(self):
      assert reverse_vowels("aA") == "Aa"