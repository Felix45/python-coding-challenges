from unittest import TestCase
from quadruplesum import quad_sum

class QuadSumTest(TestCase):
    def test_quad_sum_I(self):
        assert quad_sum([1, 0, -1, 0, -2, 2], 0) == [[-1,0,0,1],[-2,-1,1,2],[-2,0,0,2]]
    def test_quad_sum_II(self):
        assert quad_sum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]

    def test_quad_sum_III(self):
        assert quad_sum([1, 1, 1, 1, 1], 4) == [[1, 1, 1, 1]]

    def test_quad_sum_IV(self):
        assert quad_sum([1, 1, 1, 1, 1, 1], 4) == [[1, 1, 1, 1]]
