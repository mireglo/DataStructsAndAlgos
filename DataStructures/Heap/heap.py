from typing import List


class Heap:
    """
    Implementation of the Max Heap ADT. Has the following methods:
    __init__(), max(), bubble_up(int), insert(int), bubble_down(int), extract_max(int), increase_priority(int, int)
    """
    def __init__(self) -> None:
        self.heap_lst = []

    def __len__(self) -> int:
        return len(self.heap_lst)

    def max(self) -> int:
        """
        Returns the maximum value stored in the Heap
        :return: Maximum value stored in the Heap
        """
        if self.heap_lst is []:
            return None
        else:
            return self.heap_lst[0]

    def bubble_up(self, position: int) -> None:
        if position % 2 == 0:
            parent_position = (position - 2) // 2
        else:
            parent_position = (position - 1) // 2

        new_value = self.heap_lst[position]

        while position > 0 and new_value > self.heap_lst[parent_position]:
            self.heap_lst[position] = self.heap_lst[parent_position]
            self.heap_lst[parent_position] = new_value

            position = parent_position

            if position % 2 == 0:
                parent_position = (position - 2) // 2
            else:
                parent_position = (position - 1) // 2

    def insert(self, new_value: int) -> None:
        """
        Insert a value into the Heap
        :param new_value: int Value to be inserted into the Heap
        :return: None
        """
        self.heap_lst.append(new_value)
        position = len(self.heap_lst) - 1

        self.bubble_up(position)

    def bubble_down(self, position: int) -> None:
        left_child = (position * 2) + 1
        right_child = (position * 2) + 2

        while left_child < len(self.heap_lst):
            if right_child >= len(self.heap_lst) and self.heap_lst[position] < self.heap_lst[left_child]:
                temp = self.heap_lst[position]
                self.heap_lst[position] = self.heap_lst[left_child]
                self.heap_lst[left_child] = temp
                position = left_child

            elif right_child < len(self.heap_lst):
                if self.heap_lst[left_child] >= self.heap_lst[right_child] and self.heap_lst[position] < self.heap_lst[left_child]:
                    temp = self.heap_lst[position]
                    self.heap_lst[position] = self.heap_lst[left_child]
                    self.heap_lst[left_child] = temp
                    position = left_child

                elif self.heap_lst[left_child] <= self.heap_lst[right_child] and self.heap_lst[position] < self.heap_lst[right_child]:
                    temp = self.heap_lst[position]
                    self.heap_lst[position] = self.heap_lst[right_child]
                    self.heap_lst[right_child] = temp
                    position = right_child

                else:
                    break

            else:
                break

            left_child = (position * 2) + 1
            right_child = (position * 2) + 2

    def extract_max(self) -> int:
        """
        Removes and returns the largest value in the Heap
        :return: Largest value in the Heap
        """
        temp = self.heap_lst[0]
        self.heap_lst[0] = self.heap_lst[-1]

        self.heap_lst.pop()

        self.bubble_down(0)

        return temp

    def increase_priority(self, node_index: int, new_priority: int) -> None:
        """
        Increase the priority of an element at the 'node_index' of the level order traversal of the Heap
        :return: None
        """
        self.heap_lst[node_index] = new_priority
        self.bubble_up(node_index)


def build_max_heap(arr: List[int]) -> Heap:
    return_heap = Heap()
    return_heap.heap_lst = arr

    for i in range(len(return_heap)//2 - 1, -1, -1):
        return_heap.bubble_down(i)

    return return_heap
