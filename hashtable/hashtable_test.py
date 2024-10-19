from unittest import TestCase
from hashtable import HashTable

class HashTableTest(TestCase):

    def test_add(self):
        ht = HashTable(10)
        ht.add('Felix')
        ht.add('Alex')
        ht.add('Emily')

        assert ht.contains('silvia') == False
        assert ht.contains('Emily')  == True

    def test_remove(self):
        ht = HashTable(10)
        ht.add('Felix')
        ht.add('Alex')
        ht.add('Emily')

        assert ht.contains('Felix') == True
        ht.remove('Felix')
        assert ht.contains('Felix')  == False