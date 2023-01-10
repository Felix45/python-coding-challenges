from unittest import TestCase
from indexof import getOccurence

class GetOccurenceTest(TestCase):
    def test_get_occurence_h(self):
      assert getOccurence('This is a dish', 'h') == [1, 13]

    def test_get_occurence_is(self):
      assert getOccurence('This is a dish', 'is') == [2, 5, 11]
