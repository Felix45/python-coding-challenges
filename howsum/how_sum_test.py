from unittest import TestCase
from how_sum import how_sum

class HowSumTest(TestCase):
    def test_how_sum_seven(self):
      assert how_sum(7, [2, 3, 4], {}) == [3, 2, 2]

    def test_how_sum_eight(self):
      assert how_sum(8, [1, 3, 5], {}) == [1, 1, 1, 1, 1, 1, 1, 1]

    def test_how_sum_three_hundred(self):
      assert how_sum(300, [100, 3, 5], {}) == [100, 100, 100]

    def test_how_sum_three_hundred_false(self):
      assert how_sum(300, [7, 14], {}) == None
