from unittest import TestCase
from reverse_string import reverse_string

class AnagramsTest(TestCase):
    def test_reverse_string_hello(self):
      assert reverse_string(["h","e","l","l","o"]) == ["o","l","l","e","h"]

    def test_reverse_string_hannah(self):
      assert reverse_string(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]
