from __future__ import annotations
from typing import Any


class AVLTreeNode:
    """
    AVLTreeNode is the building block used to create AVL Trees. They have a 'key' attribute which is an int,
    a value which holds an object, they also have pointers 'left' and 'right' which hold the left and right subtrees.

    Each Node holds the number of nodes in its Tree in the 'size' attribute and the height of the subtree in the
    'height' attribute. They also hold a 'bf' attribute which is the balance factor (Height of Right subtree - Height
    of Left subtree)
    """
    def __init__(self, key: int, value: Any = None, left: AVLTreeNode = None, right: AVLTreeNode = None) -> None:
        self.key = key
        self.value = value
        self.parent = None
        self.left = left
        self.right = right

        if self.left is None and self.right is None:
            self.height = 0
            self.bf = 0
            self.size = 1

        elif self.left is None and self.right is not None:
            self.height = self.right.height + 1
            self.size = self.right.size + 1
            self.bf = self.right.height

        elif self.left is not None and self.right is None:
            self.height = self.left.height + 1
            self.size = self.left.size + 1
            self.bf = 0 - self.left.height

        else:
            self.height = max(self.left.height, self.right.height) + 1
            self.size = self.left.size + self.right.size + 1
            self.bf = self.right.height - self.left.height

    def update_size_height_bf(self, location: AVLTreeNode = None):
        if location is None:
            curr = self
        else:
            curr = location

        while curr is not None:
            curr.update_helper()
            curr = curr.parent

    def update_helper(self):
        if self.left is None and self.right is None:
            self.height = 0
            self.size = 1
            self.bf = 0

        elif self.left is None and self.right is not None:
            self.height = self.right.height + 1
            self.size = self.right.size + 1
            self.bf = (self.right.height + 1)

        elif self.left is not None and self.right is None:
            self.height = self.left.height + 1
            self.size = self.left.size + 1
            self.bf = 0 - (self.left.height + 1)

        else:
            self.height = max(self.left.height, self.right.height) + 1
            self.size = self.left.size + self.right.size + 1
            self.bf = (self.right.height + 1) - (self.left.height + 1)

    def insert(self, root: AVLTreeNode, key: int, value: Any) -> AVLTreeNode:
        if root is None:
            return AVLTreeNode(key, value)

        elif key <= root.key:
            root.left = self.insert(root.left, key, value)

        elif key > root.key:
            root.right = self.insert(root.right, key, value)

        root.update_helper()

        # Left Left
        if root.bf < -1 and key <= root.left.key:
            return self.right_rotate(root)

        # Right Right
        if root.bf > 1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right
        if root.bf < -1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if root.bf > 1 and key <= root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    @staticmethod
    def left_rotate(root: AVLTreeNode) -> AVLTreeNode:
        right_node = root.right
        child_left_node = right_node.left

        right_node.left = root
        root_parent = root.parent
        root.parent = right_node
        right_node.parent = root_parent

        root.right = child_left_node

        if child_left_node is not None:
            child_left_node.parent = root
            child_left_node.update_helper()

        root.update_helper()
        right_node.update_size_height_bf()

        return right_node

    @staticmethod
    def right_rotate(root: AVLTreeNode) -> AVLTreeNode:
        left_node = root.left
        child_right_node = left_node.right

        left_node.right = root
        root_parent = root.parent
        root.parent = left_node
        left_node.parent = root_parent

        root.left = child_right_node

        if child_right_node is not None:
            child_right_node.parent = root
            child_right_node.update_helper()

        root.update_helper()
        left_node.update_size_height_bf()

        return left_node

    def in_order_traversal(self) -> None:
        if self is not None:

            if self.left is not None:
                self.left.in_order_traversal()

            print(self.key)

            if self.right is not None:
                self.right.in_order_traversal()

    def pre_order_traversal(self) -> None:
        if self is not None:

            print(self.key)

            if self.left is not None:
                self.left.pre_order_traversal()

            if self.right is not None:
                self.right.pre_order_traversal()

    def post_order_traversal(self) -> None:
        if self is not None:

            if self.left is not None:
                self.left.post_order_traversal()

            if self.right is not None:
                self.right.post_order_traversal()

            print(self.key)

    def level_order_traversal(self) -> None:
        queue = [self]
        while len(queue) > 0:
            curr = queue.pop(0)
            print(curr.key)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)


class AVL:
    def __init__(self, root: AVLTreeNode = None) -> None:
        self.root = root

    def insert(self, key: int, value: Any) -> None:
        if self.root is None:
            self.root = AVLTreeNode(key, value)
        else:
            self.root = self.root.insert(self.root, key, value)

    def size(self) -> int:
        """
        Returns the size of the AVL Tree
        :return: Number of nodes in the AVL Tree
        """
        if self.root is None:
            return 0

        return self.root.size

    def height(self) -> int:
        """
        Returns the height of the AVL Tree. Returns -1 if root is None.
        :return: Height of AVL Tree
        """
        if self.root is None:
            return -1

        return self.root.height

    def in_order_traversal(self) -> None:
        """
        Prints the keys of the AVLTreeNodes by in order traversing the AVL Tree.
        :return: None
        """
        self.root.in_order_traversal()

    def pre_order_traversal(self) -> None:
        """
        Prints the keys of the AVLTreeNodes by pre order traversing the AVL Tree.
        :return: None
        """
        self.root.pre_order_traversal()

    def post_order_traversal(self) -> None:
        """
        Prints the keys of the AVLTreeNodes by post order traversing the AVL Tree.
        :return: None
        """
        self.root.post_order_traversal()

    def level_order_traversal(self) -> None:
        """
        Prints the keys of the AVLTreeNodes by level order traversing the AVL Tree.
        :return: None
        """
        self.root.level_order_traversal()
