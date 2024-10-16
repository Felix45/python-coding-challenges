from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    def test_push(self):
        st = Stack()
        st.push(5)
        st.push(4)

        assert st.peek() == 4

    def test_pop(self):
        st = Stack()
        st.push(5)
        st.push(4)
        st.push(3)
        assert st.pop() == 3

    def test_peek(self):
        st = Stack()
        st.push(5)
        st.push(4)

        assert st.peek() == 4

    def test_isEmpty(self):
        st = Stack()
        st.push(5)
        st.push(4)
        st.peek()
        st.pop()
        st.pop()

        assert st.is_empty() == True

    def test_stack_size(self):
        st = Stack()
        st.push(5)
        st.push(5)
        st.push(3)

        assert st.stack_size() == 3