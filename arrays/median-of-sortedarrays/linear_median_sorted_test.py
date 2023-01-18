from unittest import TestCase
from linear_median_sorted import linear_median_sorted

class MedainSortedArrayTest(TestCase):
    def test_linear_median_sorted_I(self):
      assert linear_median_sorted([1,3], [0,2]) == 1.5

    def test_linear_median_sorted_II(self):
      assert linear_median_sorted([1,2], [3,4]) == 2.5

    def test_linear_median_sorted_III(self):
      assert linear_median_sorted([1,3,5,6], [-3, -1, 0, 2]) == 1.5
