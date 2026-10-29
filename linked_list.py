class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def prepend(self, value):
        new_node = Node(value, next_node = self.head)
        self.head = new_node
        
        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def append(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1