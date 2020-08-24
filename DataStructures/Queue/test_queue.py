from unittest import TestCase

from DataStructures.Queue.queue import Queue, OverFlowError, UnderFlowError


class TestQueue(TestCase):
    def test_init(self):
        s = Queue(5)
        assert s.lst == []
        assert s.size == 5
        assert s.rear == -1

    def test_len(self):
        s = Queue(10)
        assert len(s) == 10

    def test_repr(self):
        s = Queue(2)

        assert s.__repr__() == 'Front --> Rear'

        s.enqueue(1)

        assert s.__repr__() == 'Front --> 1 -> Rear'

        s.enqueue(2)

        assert s.__repr__() == 'Front --> 1 -> 2 -> Rear'

        s.dequeue()

        assert s.__repr__() == 'Front --> 2 -> Rear'

        s.dequeue()

        assert s.__repr__() == 'Front --> Rear'

    def test_enqueue_int(self):
        s = Queue(3)
        assert s.lst == []
        assert s.size == 3
        assert s.rear == -1

        s.enqueue(1)
        assert s.lst == [1]
        assert s.size == 3
        assert s.rear == 0

        s.enqueue(2)
        assert s.lst == [1, 2]
        assert s.size == 3
        assert s.rear == 1

        s.enqueue(3)
        assert s.lst == [1, 2, 3]
        assert s.size == 3
        assert s.rear == 2

    def test_enqueue_str(self):
        s = Queue(3)
        assert s.lst == []
        assert s.size == 3
        assert s.rear == -1

        s.enqueue('a')
        assert s.lst == ['a']
        assert s.size == 3
        assert s.rear == 0

        s.enqueue('b')
        assert s.lst == ['a', 'b']
        assert s.size == 3
        assert s.rear == 1

        s.enqueue('c')
        assert s.lst == ['a', 'b', 'c']
        assert s.size == 3
        assert s.rear == 2

    def test_dequeue_int(self):
        s = Queue(3)

        s.enqueue(1)
        s.enqueue(2)
        s.enqueue(3)

        assert s.lst == [1, 2, 3]
        assert s.size == 3
        assert s.rear == 2

        assert s.dequeue() == 1
        assert s.lst == [2, 3]
        assert s.rear == 1

        assert s.dequeue() == 2
        assert s.lst == [3]
        assert s.rear == 0

        assert s.dequeue() == 3
        assert s.lst == []
        assert s.rear == -1

    def test_dequeue_str(self):
        s = Queue(3)

        s.enqueue('a')
        s.enqueue('b')
        s.enqueue('c')

        assert s.lst == ['a', 'b', 'c']
        assert s.size == 3
        assert s.rear == 2

        assert s.dequeue() == 'a'
        assert s.lst == ['b', 'c']
        assert s.rear == 1

        assert s.dequeue() == 'b'
        assert s.lst == ['c']
        assert s.rear == 0

        assert s.dequeue() == 'c'
        assert s.lst == []
        assert s.rear == -1

    def test_overflow(self):
        s = Queue(0)
        with self.assertRaises(OverFlowError):
            s.enqueue([])

    def test_underflow(self):
        s = Queue(0)
        with self.assertRaises(UnderFlowError):
            s.dequeue()

    def test_peek(self):
        s = Queue(3)

        assert s.peek() is None

        s.enqueue(1)
        assert s.peek() == 1

        s.enqueue(2)
        assert s.peek() == 1

        s.enqueue(3)
        assert s.peek() == 1