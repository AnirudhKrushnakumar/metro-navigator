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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def prepend(self, value):
        new_node = Node(value, next_node = self.head)
        self.head = new_node
        
        if self.tail is None:
            self.tail = new_node

        self._size += 1
    
    def _get_node(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")

        target_node = self._get_node(index)
        return target_node.value
    
    def remove_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")
        assert self.head is not None

        if index == 0:
            removed_val = self.head.value
            self.head = self.head.next
            self._size -= 1

            if self.is_empty():
                self.tail = None

            return removed_val

        prev = self._get_node(index - 1)
        target = prev.next
        assert target is not None
        
        removed_val = target.value
        prev.next = target.next

        if index == self._size - 1:
            self.tail = prev

        self._size -= 1
        return removed_val

    def remove(self, value):
        idx = self.find(value)
        if idx == -1:
            return False
        self.remove_at(idx)
        return True

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def find(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def insert_at(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(value)
            return

        if index == self._size:
            self.append(value)
            return

        prev = self._get_node(index - 1)
        new_node = Node(value, next_node=prev.next)
        prev.next = new_node
        self._size += 1

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        if self.is_empty():
            return "None"

        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"