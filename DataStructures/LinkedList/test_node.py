from unittest import TestCase

from DataStructures.LinkedList.linkedlist import Node


class TestNode(TestCase):
    def test_basic_init(self):
        x = Node(5)
        assert x.value == 5
        assert x.prevNode is None
        assert x.nextNode is None

    def test_init_prev(self):
        x = Node(5)
        y = Node(10, x)
        assert y.value == 10
        assert y.prevNode == x
        assert y.nextNode is None

    def test_init_both(self):
        x = Node(5)
        z = Node(10)
        y = Node(-10, x, z)
        assert y.value == -10
        assert y.prevNode == x
        assert y.nextNode == z
