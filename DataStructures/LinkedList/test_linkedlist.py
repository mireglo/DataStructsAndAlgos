from unittest import TestCase

from DataStructures.LinkedList.linkedlist import Node, LinkedList


class TestLinkedList(TestCase):
    def test_init_one_node(self):
        x = Node(5)
        lst = LinkedList(x)
        assert lst.head == x
        assert lst.tail == x
        assert lst.size == 1

    def test_init_two_nodes(self):
        x = Node(5)
        y = Node(-5)
        lst = LinkedList(x, y)
        assert lst.head == x
        assert lst.tail == y
        assert lst.size == 2

    def test_len(self):
        x = Node(5)
        lst1 = LinkedList(x)
        y = Node(-5)
        lst2 = LinkedList(x, y)
        assert len(lst1) == 1
        assert len(lst2) == 2

    def test_repr(self):
        x = Node('Node1')
        y = Node('Node2')
        lst = LinkedList(x, y)
        assert lst.__repr__() == "Head --> Node1 -> Node2 -> Tail"
