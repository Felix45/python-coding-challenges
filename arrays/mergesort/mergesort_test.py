from unittest import TestCase
from mergesort import mergesort

class MergeSortTest(TestCase):
    def test_mergesort_I(self):
      assert mergesort([6, 3, 5, 1], 4) == [1, 3, 5, 6]

    def test_mergesort_II(self):
      assert mergesort([-1,-3,0,2], 4) == [-3, -1, 0, 2]

    def test_mergesort_III(self):
       assert mergesort([-1,4,0,-1,-5,-6], 6) == [-6, -5, -1, -1, 0, 4]
