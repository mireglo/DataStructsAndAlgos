from typing import Any
from DataStructures.Stack.stack import OverFlowError, UnderFlowError


class Queue:
    """
    Implementation of Queue ADT. Has the following methods:
    __init__(), __len__(), __repr__(), enqueue(object), dequeue(), isEmpty(), peek()
    """

    def __init__(self, n: int) -> None:
        """
        :param n: Maximum size of Queue
        """
        self.size = n
        self.rear = -1
        self.lst = []

    def __len__(self) -> int:
        """
        Returns the maximum size of the created Queue object
        :return: self.size which is the Maximum number of objects this Queue can contain
        """
        return self.size

    def __repr__(self) -> str:
        """
        Prints a readable version of the queue.
        :return: Readable string of the queue
        """
        ret_str = 'Front --> '
        for obj in self.lst:
            ret_str += str(obj) + ' -> '
        ret_str += 'Rear'
        return ret_str

    def enqueue(self, obj: Any) -> None:
        """
        Adds an object to the queue
        :param obj: The object to be added
        :return: None
        """
        if self.rear == self.size - 1:
            raise OverFlowError()
        else:
            self.rear += 1

            self.lst.append(obj)

    def dequeue(self) -> Any:
        """
        Removes the object at the top of the queue and returns it

        :return: Object at the front of the Queue
        """
        if self.rear == -1:
            raise UnderFlowError()
        else:
            self.rear -= 1

            dequeued_element = self.lst[0]
            self.lst = self.lst[1:]

            return dequeued_element

    def peek(self) -> Any:
        """
        Returns the object at the top of the queue but doesnt remove it

        :return: Object at the top of the Queue
        """
        if self.rear == -1:
            return None
        else:
            return self.lst[0]
