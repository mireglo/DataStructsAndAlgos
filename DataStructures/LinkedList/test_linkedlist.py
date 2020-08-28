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

    def test_insert(self):
        x = Node('Node1')
        y = Node('Node2')
        lst = LinkedList(x, y)
        assert lst.__repr__() == "Head --> Node1 -> Node2 -> Tail"
        lst.insert(Node('Node0'), 0)
        assert lst.__repr__() == "Head --> Node0 -> Node1 -> Node2 -> Tail"
        lst.insert(Node('Node3'), 3)
        assert lst.__repr__() == "Head --> Node0 -> Node1 -> Node2 -> Node3 -> Tail"
        lst.insert(Node('Node2.5'), 3)
        assert lst.__repr__() == "Head --> Node0 -> Node1 -> Node2 -> Node2.5 -> Node3 -> Tail"
        lst.insert(Node('Node1.5'), 2)
        assert lst.__repr__() == "Head --> Node0 -> Node1 -> Node1.5 -> Node2 -> Node2.5 -> Node3 -> Tail"

        with self.assertRaises(IndexError):
            lst.insert(Node('Node-1'), -1)

        with self.assertRaises(IndexError):
            lst.insert(Node('Node7'), len(lst)+1)

    def test_remove(self):
        lst = LinkedList(Node('Node1'), Node('Node2'))
        lst.insert(Node('Node0'), 0)
        lst.insert(Node('Node3'), 3)
        assert lst.__repr__() == "Head --> Node0 -> Node1 -> Node2 -> Node3 -> Tail"

        assert lst.remove(1).value == "Node1"
        assert lst.__repr__() == "Head --> Node0 -> Node2 -> Node3 -> Tail"
        assert lst.remove(1).value == "Node2"
        assert lst.__repr__() == "Head --> Node0 -> Node3 -> Tail"

        with self.assertRaises(IndexError):
            lst.remove(-1)
        with self.assertRaises(IndexError):
            lst.remove(len(lst))

        assert lst.remove(0).value == "Node0"
        assert lst.__repr__() == "Head --> Node3 -> Tail"
        assert lst.remove(0).value == "Node3"
        assert lst.__repr__() == "Head --> Tail"
        assert lst.head is None
        assert lst.tail is None
        assert len(lst) == 0

    def test_find(self):
        lst = LinkedList(Node(0), Node('1'))
        lst.insert(Node([2]), 2)
        lst.insert(Node({3: 3}), 3)
        assert lst.__repr__() == "Head --> 0 -> 1 -> [2] -> {3: 3} -> Tail"

        assert lst.find({3: 3}) == 3
        assert lst.find([2]) == 2
        assert lst.find('1') == 1
        assert lst.find(0) == 0
        assert lst.find(Node(4)) == -1

    def test_reverse(self):
        lst = LinkedList(Node(0), Node('1'))
        lst.insert(Node([2]), 2)
        lst.insert(Node({3: 3}), 3)
        assert lst.__repr__() == "Head --> 0 -> 1 -> [2] -> {3: 3} -> Tail"

        lst.reverse()
        assert lst.__repr__() == "Head --> {3: 3} -> [2] -> 1 -> 0 -> Tail"
        assert lst.head.value == {3: 3}
        assert lst.tail.value == 0
