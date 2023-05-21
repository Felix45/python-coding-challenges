from unittest import TestCase
from sort_by_frequency import sort_by_frequency

class SortCharactersByFrequencyTest(TestCase):
    def test_sort_by_frequency_I(self):
      assert sort_by_frequency('tree') == 'eert'
   
    def test_sort_by_frequency_II(self):
      assert sort_by_frequency('cccaaa') == 'aaaccc'

    def test_sort_by_frequency_III(self):
      assert sort_by_frequency('Aabb') == 'bbAa'
