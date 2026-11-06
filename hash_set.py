from hash_table import HashTable

class HashSet:
    def __init__(self, capacity=8):
        self._table = HashTable(capacity=capacity)

    def __len__(self):
        return len(self._table)

    def __contains__(self, item):
        return self._table.contains(item)

    def is_empty(self):
        return len(self._table) == 0

    def clear(self):
        self._table.clear()

    def to_list(self):
        return self._table.keys()

    def add(self, item):
        exists = self._table.contains(item)
        self._table.put(item, True)
        return not exists

    def remove(self, item):
        self._table.remove(item)

    def discard(self, item):
        if self._table.contains(item):
            self._table.remove(item)
            return True
        return False

    def contains(self, item):
        return self._table.contains(item)

    def union(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        result = HashSet()
        for item in self._table.keys():
            result._table.put(item, True)
        for item in other._table.keys():
            result._table.put(item, True)
        return result

    def intersection(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        result = HashSet()
        other_table = other._table
        for item in self._table.keys():
            if other_table.contains(item):
                result._table.put(item, True)
        return result

    def difference(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        result = HashSet()
        other_table = other._table
        for item in self._table.keys():
            if not other_table.contains(item):
                result._table.put(item, True)
        return result

    def symmetric_difference(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        result = HashSet()
        other_table = other._table
        for item in self._table.keys():
            if not other_table.contains(item):
                result._table.put(item, True)
        for item in other._table.keys():
            if not self._table.contains(item):
                result._table.put(item, True)
        return result

    def is_subset(self, other):
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")
        other_table = other._table
        for item in self._table.keys():
            if not other_table.contains(item):
                return False
        return True