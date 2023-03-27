from unittest import TestCase
from missing_number import missing_number

class MissingNumberTest(TestCase):
    def test_missing_number_I(self):
      assert missing_number([1, 3, 6, 4, 1, 2]) == 5

    def test_missing_number_II(self):
      assert missing_number([1, 2, 3]) == 4

    def test_missing_number_III(self):
       assert missing_number([-1, -3]) == 1
