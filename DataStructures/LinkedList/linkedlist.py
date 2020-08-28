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
    __init__(), __len__(), __repr__(), __iter__(), __next__(), insert(n), remove(n), find(obj), is_empty()
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

    def is_empty(self) -> bool:
        """
        Return true if Linked List has no elements
        :return: Boolean True if Linked List size is 0
        """
        return len(self) == 0

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

        elif position == 0 and self.size == 0:
            obj.prevNode = None
            obj.nextNode = None
            self.head = obj
            self.tail = obj
            self.size += 1

        elif position == 0:
            obj.prevNode = None
            obj.nextNode = self.head
            self.head = obj
            self.size += 1

        elif position == self.size:
            obj.prevNode = self.tail
            obj.nextNode = None
            self.tail.nextNode = obj
            self.tail = obj
            self.size += 1

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

            self.size += 1

    def remove(self, position: int) -> Any:
        """
        Remove a Node from the Linked List at index 'position' and return it. If position is out of range of the Linked
        List, then we raise an IndexError. Valid positions are integers between 0 and self.size both inclusive.
        :param position: Index to insert the object in the Linked List
        :return: Node removed from the Linked List
        """
        if position >= self.size or position < 0:
            raise IndexError

        elif position == 0 and self.size == 1:
            return_node = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return return_node

        elif position == 0:
            return_node = self.head
            self.head = self.head.nextNode
            self.size -= 1
            return return_node

        elif position == self.size:
            return_node = self.tail
            self.tail = self.tail.prevNode
            self.size -= 1
            return return_node

        else:
            index = 0
            curr_node = self.head

            while index < position - 1:
                index += 1
                curr_node = curr_node.nextNode

            left_node = curr_node
            return_node = curr_node.nextNode
            right_node = return_node.nextNode
            left_node.nextNode = right_node
            right_node.prevNode = left_node

            self.size -= 1
            return return_node

    def find(self, obj: Any) -> int:
        """
        Looks for the object as a value for a Node in the Linked List. If found returns the index of the Node otherwise
        it returns -1
        :param obj: Object to find in the Linked List
        :return: Index of Node with Object in Linked List or -1 if not found
        """
        curr_node = self.head
        index = 0
        while curr_node is not None:
            if curr_node.value == obj:
                return index
            curr_node = curr_node.nextNode
            index += 1
        return -1

    def reverse(self) -> None:
        """
        Reverses the Linked List
        :return: None
        """
        if self.size > 1:
            curr = self.head

            while curr is not None:
                prev_node = curr.prevNode
                curr.prevNode = curr.nextNode
                curr.nextNode = prev_node
                curr = curr.prevNode

            temp = self.head
            self.head = self.tail
            self.tail = temp
