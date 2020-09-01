from unittest import TestCase

from DataStructures.Heap.heap import Heap, build_max_heap


class TestHeap(TestCase):
    def test_init(self):
        h = Heap()
        assert h.heap_lst == []

    def test_insert(self):
        h = Heap()
        h.insert(0)
        h.insert(1)
        h.insert(2)
        h.insert(3)
        h.insert(4)
        h.insert(5)
        h.insert(6)

        assert h.heap_lst == [6, 3, 5, 0, 2, 1, 4]

    def test_max(self):
        h = Heap()
        h.insert(0)
        h.insert(1)
        h.insert(2)
        h.insert(3)
        h.insert(4)
        h.insert(5)
        h.insert(6)
        assert h.max() == 6
        h.insert(-6)
        assert h.max() == 6
        h.insert(20)
        assert h.max() == 20

    def test_extract_max(self):
        h = Heap()
        h.insert(0)
        h.insert(1)
        h.insert(2)
        h.insert(3)
        h.insert(4)
        h.insert(5)
        h.insert(6)

        assert h.extract_max() == 6
        assert h.heap_lst == [5, 3, 4, 0, 2, 1]

        assert h.extract_max() == 5
        assert h.heap_lst == [4, 3, 1, 0, 2]

        assert h.extract_max() == 4
        assert h.heap_lst == [3, 2, 1, 0]

        assert h.extract_max() == 3
        assert h.heap_lst == [2, 0, 1]

        assert h.extract_max() == 2
        assert h.heap_lst == [1, 0]

        assert h.extract_max() == 1
        assert h.heap_lst == [0]

        assert h.extract_max() == 0
        assert h.heap_lst == []

    def test_increase_priority(self):
        h = Heap()
        h.insert(0)
        h.insert(1)
        h.insert(2)
        h.insert(3)
        h.insert(4)
        h.insert(5)
        h.insert(6)

        h.increase_priority(0, 7)
        assert h.heap_lst == [7, 3, 5, 0, 2, 1, 4]

        h.increase_priority(3, 8)
        assert h.heap_lst == [8, 7, 5, 3, 2, 1, 4]

        h.increase_priority(3, 4)
        assert h.heap_lst == [8, 7, 5, 4, 2, 1, 4]

    def test_build_max_heap(self):
        arr = [23, 33, 45, 31, 44, 51, 20, 65, 37, 18, 12, 70, 49, 28, 29]
        h = build_max_heap(arr)
        print(h.heap_lst)
        assert h.heap_lst == [70, 65, 51, 37, 44, 49, 29, 31, 33, 18, 12, 45, 23, 28, 20]
