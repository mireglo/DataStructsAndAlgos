from __future__ import annotations

from typing import Any, Optional


class TreeNode:
    """
    TreeNode is the building block used to create Trees. They have a 'key' attribute which is an int, a value which
    holds an object, they also have pointers 'left' and 'right' which hold the left and right subtrees.

    Each Node holds the number of nodes in its Tree in the 'size' attribute and the height of the subtree in the
    'height' attribute.
    """
    def __init__(self, key: int, value: Any, left: TreeNode = None, right: TreeNode = None) -> None:
        self.key = key
        self.value = value
        self.parent = None
        self.left = left
        self.right = right

        if self.left is None and self.right is None:
            self.height = 0
            self.size = 1

        elif self.left is None and self.right is not None:
            self.height = self.right.height + 1
            self.size = self.right.size + 1

        elif self.left is not None and self.right is None:
            self.height = self.left.height + 1
            self.size = self.left.size + 1

        else:
            self.height = max(self.left.height, self.right.height) + 1
            self.size = self.left.size + self.right.size + 1

    def update_size_height(self):
        curr = self

        while curr is not None:
            if curr.left is None and curr.right is None:
                curr.height = 0
                curr.size = 1

            elif curr.left is None and curr.right is not None:
                curr.height = curr.right.height + 1
                curr.size = curr.right.size + 1

            elif curr.left is not None and curr.right is None:
                curr.height = curr.left.height + 1
                curr.size = curr.left.size + 1

            else:
                curr.height = max(curr.left.height, curr.right.height) + 1
                curr.size = curr.left.size + curr.right.size + 1

            curr = curr.parent

    def insert(self, key: int, value: Any) -> None:
        if key <= self.key:
            if self.left is None:
                self.left = TreeNode(key, value)
                self.left.parent = self
                self.update_size_height()
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.right = TreeNode(key, value)
                self.right.parent = self
                self.update_size_height()
            else:
                self.right.insert(key, value)

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


class BST:
    """
    Implementation of the Binary Search Tree ADT. Has the following methods:
    __init__(TreeNode=None), insert(int, Any), size(), height(), in_order_traversal(),
    pre_order_traversal(), post_order_traversal(), level_order_traversal()
    """
    def __init__(self, root: TreeNode = None) -> None:
        self.root = root

    def insert(self, key: int, value: Any) -> None:
        """
        Inserts a TreeNode with the given key and value into the BST
        :param key: key of the TreeNode
        :param value: Object/Value stored in the TreeNode
        :return: None
        """
        if self.root is None:
            self.root = TreeNode(key, value)

        else:
            self.root.insert(key, value)

    def size(self) -> int:
        """
        Returns the size of the BST
        :return: Number of nodes in the BSt
        """
        if self.root is None:
            return 0

        return self.root.size

    def height(self) -> int:
        """
        Returns the height of the BST. Returns -1 if root is None.
        :return: Height of BST
        """
        if self.root is None:
            return -1

        return self.root.height

    def in_order_traversal(self) -> None:
        """
        Prints the keys of the TreeNodes by in order traversing the BST.
        :return: None
        """
        self.root.in_order_traversal()

    def pre_order_traversal(self) -> None:
        """
        Prints the keys of the TreeNodes by pre order traversing the BST.
        :return: None
        """
        self.root.pre_order_traversal()

    def post_order_traversal(self) -> None:
        """
        Prints the keys of the TreeNodes by post order traversing the BST.
        :return: None
        """
        self.root.post_order_traversal()

    def level_order_traversal(self) -> None:
        """
        Prints the keys of the TreeNodes by level order traversing the BST.
        :return: None
        """
        self.root.level_order_traversal()
