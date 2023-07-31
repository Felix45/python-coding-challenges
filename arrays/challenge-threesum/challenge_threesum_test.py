from unittest import TestCase
from challenge_threesum import three_sum

class ThreeSumTest(TestCase):
    def test_threesum_I(self):
      assert three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]

    def test_three_sum_II(self):
      assert three_sum([0,1,1]) == []

    def test_three_sum_III(self):
      assert three_sum([0,0,0]) == [[0,0,0]]
