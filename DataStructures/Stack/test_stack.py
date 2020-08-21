from unittest import TestCase

from DataStructures.Stack.stack import Stack, OverFlowError, UnderFlowError


class TestStack(TestCase):
    def test_init(self):
        s = Stack(5)
        assert s.lst == []
        assert s.size == 5
        assert s.top == -1

    def test_len(self):
        s = Stack(10)
        assert len(s) == 10

    def test_repr(self):
        s = Stack(2)

        assert s.__repr__() == 'Top --> '

        s.push(1)

        assert s.__repr__() == 'Top --> 1 -> '

        s.push(2)

        assert s.__repr__() == 'Top --> 2 -> 1 -> '

        s.pop()

        assert s.__repr__() == 'Top --> 1 -> '

        s.pop()

        assert s.__repr__() == 'Top --> '

    def test_push_int(self):
        s = Stack(3)
        assert s.lst == []
        assert s.size == 3
        assert s.top == -1

        s.push(1)
        assert s.lst == [1]
        assert s.size == 3
        assert s.top == 0

        s.push(2)
        assert s.lst == [1, 2]
        assert s.size == 3
        assert s.top == 1

        s.push(3)
        assert s.lst == [1, 2, 3]
        assert s.size == 3
        assert s.top == 2

    def test_push_str(self):
        s = Stack(3)
        assert s.lst == []
        assert s.size == 3
        assert s.top == -1

        s.push('a')
        assert s.lst == ['a']
        assert s.size == 3
        assert s.top == 0

        s.push('b')
        assert s.lst == ['a', 'b']
        assert s.size == 3
        assert s.top == 1

        s.push('c')
        assert s.lst == ['a', 'b', 'c']
        assert s.size == 3
        assert s.top == 2

    def test_pop_int(self):
        s = Stack(3)

        s.push(1)
        s.push(2)
        s.push(3)

        assert s.lst == [1, 2, 3]
        assert s.size == 3
        assert s.top == 2

        assert s.pop() == 3
        assert s.lst == [1, 2]
        assert s.top == 1

        assert s.pop() == 2
        assert s.lst == [1]
        assert s.top == 0

        assert s.pop() == 1
        assert s.lst == []
        assert s.top == -1

    def test_pop_str(self):
        s = Stack(3)

        s.push('a')
        s.push('b')
        s.push('c')

        assert s.lst == ['a', 'b', 'c']
        assert s.size == 3
        assert s.top == 2

        assert s.pop() == 'c'
        assert s.lst == ['a', 'b']
        assert s.top == 1

        assert s.pop() == 'b'
        assert s.lst == ['a']
        assert s.top == 0

        assert s.pop() == 'a'
        assert s.lst == []
        assert s.top == -1

    def test_overflow(self):
        s = Stack(0)
        with self.assertRaises(OverFlowError):
            s.push([])

    def test_underflow(self):
        s = Stack(0)
        with self.assertRaises(UnderFlowError):
            s.pop()

    def test_peek(self):
        s = Stack(3)

        assert s.peek() is None

        s.push(1)
        assert s.peek() == 1

        s.push(2)
        assert s.peek() == 2

        s.push(3)
        assert s.peek() == 3