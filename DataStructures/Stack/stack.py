from typing import Any


class OverFlowError(Exception):
    """
    Exception raised when Stack overflows.
    (Pushing an object onto a full Stack)
    """
    def __init__(self):
        super().__init__(self, "Overflow Error")


class UnderFlowError(Exception):
    """
    Exception raised when Stack underflows.
    (Popping an object from an empty Stack)
    """
    def __init__(self):
        super().__init__(self, "Underflow Error")


class Stack:
    """
    Implementation of Stack ADT. Has the following methods:
    __init__(), __len__(), __repr__(), push(object), pop(), isEmpty(), peek()
    """

    def __init__(self, n: int) -> None:
        """
        :param n: Maximum size of Stack
        """
        self.size = n
        self.top = -1
        self.lst = []

    def __len__(self) -> int:
        """
        Returns the maximum size of the created Stack object
        :return: self.size which is the Maximum number of objects this Stack can contain
        """
        return self.size

    def __repr__(self) -> str:
        """
        Prints a readable version of the stack.
        :return: Readable string of the Stack
        """
        ret_str = 'Top --> '
        for obj in self.lst[::-1]:
            ret_str += str(obj) + ' -> '
        return ret_str

    def push(self, obj: Any) -> None:
        """
        Adds an object to the stack
        :param obj: The object to be added
        :return: None
        """
        if self.top == self.size - 1:
            raise OverFlowError()
        else:
            self.top += 1
            self.lst.append(obj)

    def pop(self) -> Any:
        """
        Removes the object at the top of the stack and returns it

        :return: Object at the top of the Stack
        """
        if self.top == -1:
            raise UnderFlowError()
        else:
            self.top -= 1
            return self.lst.pop()

    def peek(self) -> Any:
        """
        Returns the object at the top of the stack but doesnt remove it

        :return: Object at the top of the Stack
        """
        if self.top == -1:
            return None
        else:
            return self.lst[self.top]