from unittest import TestCase
from search_insert import search_insert_index

class SearchInsertTest(TestCase):
    def test_search_insert_five(self):
      assert search_insert_index([1,3,5,6], 5) == 2

    def test_search_insert_two(self):
      assert search_insert_index([1,3,5,6], 2) == 1

    def test_search_insert_seven(self):
      assert search_insert_index([1,3,5,6], 7) == 4
