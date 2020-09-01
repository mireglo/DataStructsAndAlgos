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
    def __init__(self, key: int, value: Any, left: AVLTreeNode = None, right: AVLTreeNode = None) -> None:
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

    def update_size_height_bf(self):
        curr = self

        while curr is not None:
            if curr.left is None and curr.right is None:
                curr.height = 0
                curr.size = 1
                curr.bf = 0

            elif curr.left is None and curr.right is not None:
                curr.height = curr.right.height + 1
                curr.size = curr.right.size + 1
                curr.bf = curr.right.height

            elif curr.left is not None and curr.right is None:
                curr.height = curr.left.height + 1
                curr.size = curr.left.size + 1
                curr.bf = 0 - curr.left.height

            else:
                curr.height = max(curr.left.height, curr.right.height) + 1
                curr.size = curr.left.size + curr.right.size + 1
                curr.bf = curr.right.height - curr.left.height

            curr = curr.parent

    def insert(self, key: int, value: Any) -> None:
        if key <= self.key:
            if self.left is None:
                self.left = AVLTreeNode(key, value)
                self.left.parent = self
                self.update_size_height_bf()
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.right = AVLTreeNode(key, value)
                self.right.parent = self
                self.update_size_height_bf()
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
