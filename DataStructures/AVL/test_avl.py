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
