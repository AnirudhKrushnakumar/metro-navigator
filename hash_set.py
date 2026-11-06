from hash_table import HashTable

class HashSet:
    def __init__(self, capacity=10):
        self.table = HashTable(capacity=capacity)
        self.list = self.table
        self._list = self.table

    def __len__(self):
        return len(self.table)

    def __contains__(self, item):
        return self.table.contains(item)

    def is_empty(self):
        return len(self.table) == 0

    def clear(self):
        self.table.clear()

    def to_list(self):
        return self.table.keys()

    def add(self, item):
        exists = self.table.contains(item)
        self.table.put(item, True)
        return not exists

    def remove(self, item):
        self.table.remove(item)

    def discard(self, item):
        if self.table.contains(item):
            self.table.remove(item)
            return True
        return False

    def contains(self, item):
        return self.table.contains(item)

    def union(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        result = HashSet()
        for item in self.table.keys():
            result.table.put(item, True)
        for item in other.table.keys():
            result.table.put(item, True)
        return result

    def intersection(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        result = HashSet()
        other_table = other.table
        for item in self.table.keys():
            if other_table.contains(item):
                result.table.put(item, True)
        return result

    def difference(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        result = HashSet()
        other_table = other.table
        for item in self.table.keys():
            if not other_table.contains(item):
                result.table.put(item, True)
        return result

    def symmetric_difference(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        result = HashSet()
        other_table = other.table
        for item in self.table.keys():
            if not other_table.contains(item):
                result.table.put(item, True)
        for item in other.table.keys():
            if not self.table.contains(item):
                result.table.put(item, True)
        return result

    def is_subset(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        other_table = other.table
        for item in self.table.keys():
            if not other_table.contains(item):
                return False
        return True