from unittest import TestCase
from permutation_sequence import permutation_sequence

class PermutationSequence(TestCase):
  ''' Unit test for the permutation sequence function '''
  def test_permutation_sequence_I(self):
    assert permutation_sequence(3,3) == "213"

  def test_permutation_sequence_II(self):
    assert permutation_sequence(4,9) == "2314"

  def test_permutation_sequence_III(self):
    assert permutation_sequence(3,1) == "123"
