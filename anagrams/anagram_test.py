from unittest import TestCase
from anagrams import are_anagrams_three

class AnagramsTest(TestCase):
    def test_are_anagrams_three_listen_silent(self):
      assert are_anagrams_three('Listen', 'Silent') == True

    def test_are_anagrams_three_ttew_tetw(self):
      assert are_anagrams_three('ttew', 'tetw') == True

    def test_are_anagrams_three_restful_fluster(self):
      assert are_anagrams_three('ResTfuL', 'FLUSter') == True

    def test_are_anagrams_three_anagram_nagaram(self):
      assert are_anagrams_three('anagram', 'nagaram') == True
