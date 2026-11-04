from linked_list import LinkedList

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self._size = 0
        self.buckets = [LinkedList() for _ in range(capacity)]

    def _hash(self, key):
        return abs(hash(key)) % self.capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0