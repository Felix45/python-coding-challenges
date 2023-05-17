from unittest import TestCase
from lcs import lcs

class LongestCommonSubsequenceTest(TestCase):
    def test_lcs_I(self):
      assert lcs('abcde', 'ace') == 3
   
    def test_lcs_II(self):
      assert lcs('abc', 'abc') == 3

    def test_lcs_III(self):
      assert lcs('abc', 'def') == 0
