from unittest import TestCase
from can_construct import can_construct

class BestSumTest(TestCase):
    def test_can_construct_abcdef(self):
      assert can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) == True

    def test_can_construct_skateboard(self):
      assert can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) == False

    def test_can_construct_enterapotentpot(self):
      assert can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']) == True

    def test_can_construct_longeef(self):
      assert can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']) == False

