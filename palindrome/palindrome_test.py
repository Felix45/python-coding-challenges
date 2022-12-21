from unittest import TestCase
from palindrome import is_palindrome_two

class PalindromeTest(TestCase):
    def test_is_palindrome_two_racecar(self):
      assert is_palindrome_two('racecar') == True

    def test_is_palindrome_two_amana(self):
      assert is_palindrome_two('A man, a plan, a canal: Panama') == True

    def test_is_palindrome_two_malayalam(self):
      assert is_palindrome_two('malayalam') == True

    def test_is_palindrome_two_raceacar(self):
      assert is_palindrome_two('race a car') == False
