from unittest import TestCase

from DataStructures.AVL.avl import AVL, AVLTreeNode


class TestAVL(TestCase):
    def test_insert(self):
        avl = AVL()
        avl.insert(10, "Node10")
        avl.insert(20, "Node20")
        avl.insert(30, "Node30")
        avl.insert(40, "Node40")
        avl.insert(50, "Node50")
        avl.insert(25, "Node25")

        avl.pre_order_traversal()

    def test_insert_LL(self):
        avl = AVL()
        avl.insert(2, "Node2")
        avl.insert(1, "Node1")
        avl.insert(0, "Node0")

        avl.pre_order_traversal()

    def test_insert_RR(self):
        avl = AVL()
        avl.insert(0, "Node0")
        avl.insert(1, "Node1")
        avl.insert(2, "Node2")

        avl.pre_order_traversal()

    def test_insert_LR(self):
        avl = AVL()
        avl.insert(2, "Node2")
        avl.insert(0, "Node0")
        avl.insert(1, "Node1")

        avl.pre_order_traversal()

    def test_insert_RL(self):
        avl = AVL()
        avl.insert(0, "Node0")
        avl.insert(2, "Node2")
        avl.insert(1, "Node1")

        avl.pre_order_traversal()
