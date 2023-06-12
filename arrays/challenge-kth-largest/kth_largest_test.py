from unittest import TestCase
from kth_largest_numbers import kth_largest_number

class KthLargestTest(TestCase):
    def test_kth_largest_number_I(self):
      assert kth_largest_number([12, 5, 787, 1, 23], 2) == [787, 23]

    def test_kth_largest_number_II(self):
      assert kth_largest_number([1, 23, 12, 9, 30, 2, 50], 3) == [50, 30, 23]

    def test_kth_largest_number_III(self):
       assert kth_largest_number([1, 20, 8, -7], 3) == [20, 8, 1]
