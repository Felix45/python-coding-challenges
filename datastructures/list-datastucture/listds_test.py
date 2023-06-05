from unittest import TestCase
from listds import List

class ListDataStructure(TestCase):
    ''' Thi class tests the list datastructure '''
    def test_append_list_data_structure(self):
      groceryList = List()
      groceryList.append('Apples')
      groceryList.append('Oranges')
      assert groceryList.listSize == 2

    def test_clear_data_structure(self):
      groceryList = List()
      groceryList.append('Biscuits')
      groceryList.clear()
      assert groceryList.listSize == 0

    def test_current_element(self):
      groceryList = List()
      groceryList.append('Books')
      groceryList.append('Jolyne')
      groceryList.next()
      assert groceryList.getElement() == 'Jolyne'

    def test_prev_element(self):
      booklist = List()
      booklist.append('Introduction to programming')
      booklist.append('Data structures and algorithms')
      booklist.append('Java Methods & algorithms')
      booklist.next()
      booklist.next()
      booklist.prev()
      assert booklist.getElement() == 'Data structures and algorithms' 

