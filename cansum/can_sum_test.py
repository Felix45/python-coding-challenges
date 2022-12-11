from unittest import TestCase
from can_sum import can_sum

class CanSumTest(TestCase):
    def test_can_sum_by_7(self):
      assert can_sum(7, [5, 3, 4, 7]) == True
    
    def test_can_sum_by_6(self):
      assert can_sum(6, [2, 4]) == True

    def test_can_sum_by_8(self):
      assert can_sum(8, [2, 4, 3]) == True
