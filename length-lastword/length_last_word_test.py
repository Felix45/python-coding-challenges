from unittest import TestCase
from length_last_word import length_of_last_word

class LengthOfLastWordTest(TestCase):
    def test_length_of_last_word_hello(self):
      assert length_of_last_word('Hello World') == 5

    def test_length_of_last_word_fly(self):
      assert length_of_last_word('   fly me   to   the moon  ') == 4

    def test_length_of_last_word_luffy(self):
      assert length_of_last_word('luffy is still joyboy') == 6

