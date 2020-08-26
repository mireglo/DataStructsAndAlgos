from __future__ import annotations

from typing import Any


class Node:
    """
    Node is the building block used to create Linked Lists. They have a value which holds an object, they also have
    pointers next_node and prev_node which hold the node in front or behind them in the Linked List
    """
    def __init__(self, value: any, prev_node: Node = None, next_node: Node = None):
        self.value = value
        self.prevNode = prev_node
        self.nextNode = next_node


class LinkedList:
    """
    Implementation of Double Linked List ADT. Has the following methods:
    __init__(), __len__(), __repr__(), __iter__(), __next__(), insert(n), remove(n), find(obj), isEmpty()
    """

    def __init__(self, head: Node, tail: Node = None) -> None:
        """
        :param head: First Node in the Linked List
        """
        self.head = head
        if tail is None:
            self.tail = head
            self.size = 1
        else:
            self.tail = tail
            self.head.nextNode = self.tail
            self.tail.prevNode = self.head
            self.size = 2

    def __len__(self) -> int:
        """
        :return: Size of the Linked List
        """
        return self.size

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if self.curr is None:
            raise StopIteration

        else:
            ret_node = self.curr
            self.curr = self.curr.nextNode
            return ret_node

    def __repr__(self) -> str:
        """
        Prints a readable version of the queue.
        :return: Readable string of the queue
        """
        ret_str = "Head --> "
        for node in self:
            ret_str += str(node.value) + " -> "
        ret_str += "Tail"
        return ret_str

    def insert(self, obj: Node, position: int) -> None:
        """
        Insert a Node into the Linked List at index 'position'. If position is out of range of the Linked List,
        then we raise an IndexError. Valid positions are integers between 0 and self.size both inclusive.
        :param obj: Node to insert
        :param position: Index to insert the object in the Linked List
        :return: None
        """
        if position > self.size or position < 0:
            raise IndexError

        elif position == self.size:
            obj.prevNode = self.tail
            obj.nextNode = None
            self.tail = obj

        elif position == 0:
            obj.prevNode = None
            obj.nextNode = self.head
            self.head = obj

        else:
            index = 0
            curr_node = self.head

            while index < position - 1:
                index += 1
                curr_node = curr_node.nextNode

            left_node = curr_node
            right_node = curr_node.nextNode
            left_node.nextNode = obj
            obj.prevNode = left_node
            obj.nextNode = right_node
            right_node.prevNode = obj
