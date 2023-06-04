from dataclasses import dataclass
from random import randrange


@dataclass
class Node:
    value: int = 0
    next: 'Node' = None
    prev: 'Node' = None


@dataclass
class LinkedList:
    head: 'Node' = None
    tail: 'Node' = None
    init: bool = True

    def from_list(self, array: list):
        for element in array:
            self.append(element)

    def push(self, value: int):
        new_node = Node(value)
        if self.init:
            self.tail = new_node
            self.init = False
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def append(self, value: int):
        new_node = Node(value)
        if self.init:
            self.head = new_node
            self.init = False
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    def __len__(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def get_node(self, index):
        if index >= len(self):
            return None
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def pop(self, index):
        node = self.get_node(index)
        next_node = node.next
        prev_node = node.prev
        if index == 0:
            self.head = next_node
        if index == len(self) - 1:
            self.tail = prev_node
        if next_node is not None:
            next_node.prev = prev_node
        if prev_node is not None:
            prev_node.next = next_node
        return node.value

    def clean(self):
        node = self.head
        values = []
        index = 0
        while node is not None:
            if node.value in values:
                self.pop(index)
            else:
                values.append(node.value)
                index += 1
            node = node.next

    def __str__(self):
        node = self.head
        list_values = []
        while node is not None:
            list_values.append(str(node.value))
            node = node.next
        return ", ".join(list_values)


def make_a_list(n: int, limit: int):
    return [randrange(limit + 1) for el in range(0, n)]


if __name__ == "__main__":
    inputs = make_a_list(40, 20)
    print(inputs)
    myList = LinkedList()
    for _input in inputs:
        myList.append(_input)
    myList.clean()
    print(myList)
