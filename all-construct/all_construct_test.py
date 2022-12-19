from unittest import TestCase
from all_construct import all_construct

class AllConstructTest(TestCase):
    def test_all_construct_abcdef(self):
      assert all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'ef', 'abcd', 'c']) == [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]

    def test_all_construct_purple(self):
      assert all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) == [['purp', 'le'], ['p', 'ur', 'p', 'le']]

    def test_all_construct_hello(self):
      assert all_construct('hello', ['cat', 'dog', 'mouse']) == []
