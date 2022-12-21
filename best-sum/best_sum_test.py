from unittest import TestCase
from best_sum import best_sum

class BestSumTest(TestCase):
    def test_best_sum_seven(self):
      assert best_sum(7, [2, 3, 4], {}) == [4, 3]

    def test_best_sum_eight(self):
      assert best_sum(8, [1, 3, 5], {}) == [5, 3]

    def test_best_sum_three_hundred(self):
      assert best_sum(300, [100, 3, 5], {}) == [100, 100, 100]

    def test_best_sum_one_hundred(self):
      assert best_sum(100, [1, 2, 5, 25], {}) == [25, 25, 25, 25]

    def test_best_sum_three_hundred_false(self):
      assert best_sum(300, [7, 14], {}) == None
