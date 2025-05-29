from unittest import TestCase
from intervals import mergeIntervals


class MergeIntervalsTest(TestCase):
    ''' Tests the mergeIntervals function '''

    def test_mergeIntervals_I(self):
        assert(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]])

    def test_mergeIntervals_II(self):
        assert(mergeIntervals([[1,4],[4,5]]) == [[1,5]])

    def test_mergeIntervals_III(self):
        assert(mergeIntervals([[1,4],[4,5], [0,3]]) == [[0,5]])