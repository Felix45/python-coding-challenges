from unittest import TestCase
from permutation import checkInclusion

class PermutationStringTest(TestCase):
    def test_permutation_ab_eidbaooo(self):
      assert checkInclusion('ab', 'eidabaoo') == True
   
    def test_permutation_ab_eidboaoo(self):
      assert checkInclusion('ab','eidboaoo') == False

    def test_permutation_prosperity_properties(self):
      assert checkInclusion('prosperity','properties') == False
