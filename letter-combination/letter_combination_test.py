from unittest import TestCase
from letter_combination import letter_combination

class LetterCombinationTest(TestCase):
    def test_letter_combination_I(self):
      assert letter_combination('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
   
    def test_letter_combination_II(self):
      assert letter_combination('2') == ['a', 'b', 'c']

    def test_letter_combination_III(self):
      assert letter_combination('') == []

    def test_letter_combination_IV(self):
       assert letter_combination('45') == ["gj","gk","gl","hj","hk","hl","ij","ik","il"]
