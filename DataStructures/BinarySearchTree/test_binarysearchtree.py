from unittest import TestCase

from DataStructures.BinarySearchTree.binarysearchtree import BST, TreeNode


class TestBST(TestCase):
    def test_init_none(self):
        empty_bst = BST()
        assert empty_bst.root is None
        assert empty_bst.size() == 0
        assert empty_bst.height() == -1

    def test_init(self):
        bst = BST(TreeNode(0, 'RootNode'))
        assert bst.root.key == 0
        assert bst.root.value == 'RootNode'
        assert bst.size() == 1
        assert bst.height() == 0

    def test_insert(self):
        bst = BST(TreeNode(0, 'RootNode'))
        bst.insert(-1, 'LeftNode')
        bst.insert(1, 'RightNode')
        assert bst.size() == 3
        assert bst.height() == 1
        assert bst.root.left.key == -1
        assert bst.root.right.key == 1
        assert bst.root.left.parent == bst.root.right.parent == bst.root

        bst.insert(-2, 'LeftNode2')
        assert bst.root.left.left.key == -2
        bst.insert(2, 'RightNode2')
        assert bst.root.right.right.key == -2

    def test_inorder(self):
        bst = BST(TreeNode(0, 'Node0'))
        bst.insert(-2, 'Node-2')
        bst.insert(2, 'Node2')
        bst.insert(-3, 'Node-3')
        bst.insert(3, 'Node3')
        bst.insert(-1, 'Node-1')
        bst.insert(1, 'Node1')

        """
                  0
            -2          2
        -3      -1  1       3
        """

        bst.in_order_traversal()

    def test_preorder(self):
        bst = BST(TreeNode(0, 'Node0'))
        bst.insert(-2, 'Node-2')
        bst.insert(2, 'Node2')
        bst.insert(-3, 'Node-3')
        bst.insert(3, 'Node3')
        bst.insert(-1, 'Node-1')
        bst.insert(1, 'Node1')

        """
                  0
            -2          2
        -3      -1  1       3
        """

        bst.pre_order_traversal()

    def test_postorder(self):
        bst = BST(TreeNode(0, 'Node0'))
        bst.insert(-2, 'Node-2')
        bst.insert(2, 'Node2')
        bst.insert(-3, 'Node-3')
        bst.insert(3, 'Node3')
        bst.insert(-1, 'Node-1')
        bst.insert(1, 'Node1')

        """
                  0
            -2          2
        -3      -1  1       3
        """

        bst.post_order_traversal()

    def test_levelorder(self):
        bst = BST(TreeNode(0, 'Node0'))
        bst.insert(-2, 'Node-2')
        bst.insert(2, 'Node2')
        bst.insert(-3, 'Node-3')
        bst.insert(3, 'Node3')
        bst.insert(-1, 'Node-1')
        bst.insert(1, 'Node1')

        """
                  0
            -2          2
        -3      -1  1       3
        """

        bst.level_order_traversal()
