from hash_table import HashTable

class HashSet:
    def __init__(self, capacity=10):
        self.list = self.table
        self._list = self.table

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return len(self.table) == 0

    def clear(self):
        self.table.clear()

    def to_list(self):
        return self.table.keys()