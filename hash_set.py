from hash_table import HashTable


class HashSet:
    """A set of unique strings, stored as the keys of a HashTable."""

    def __init__(self, capacity=8):
        """Create an empty set whose table starts with the given capacity."""
        self._table = HashTable(capacity=capacity)

    def __len__(self):
        """Return the number of items in the set."""
        return len(self._table)

    def __contains__(self, item):
        """Support `item in set`."""
        return self._table.contains(item)

    def is_empty(self):
        """Return True if the set has no items."""
        return len(self._table) == 0

    def clear(self):
        """Remove every item from the set."""
        self._table.clear()

    def to_list(self):
        """Return a new list of the items (the order is not guaranteed)."""
        return self._table.keys()

    def add(self, item):
        """Add item.

        Returns:
            True if item was new, False if it was already in the set.
        """
        exists = self._table.contains(item)
        self._table.put(item, True)
        return not exists

    def remove(self, item):
        """Remove item.

        Raises:
            KeyError: if item is not in the set.
        """
        self._table.remove(item)

    def discard(self, item):
        """Remove item if present.

        Returns:
            True if item was removed, False if it was not in the set.
        """
        if self._table.contains(item):
            self._table.remove(item)
            return True
        return False

    def contains(self, item):
        """Return True if item is in the set."""
        return self._table.contains(item)

    def _require_hashset(self, other):
        """Raise TypeError if other is not a HashSet."""
        if not isinstance(other, HashSet):
            raise TypeError("Operand must be a HashSet")

    def union(self, other):
        """Return a new HashSet with the items that are in either set.

        Raises:
            TypeError: if other is not a HashSet.
        """
        self._require_hashset(other)
        result = HashSet()
        for item in self._table.keys():
            result._table.put(item, True)
        for item in other._table.keys():
            result._table.put(item, True)
        return result

    def intersection(self, other):
        """Return a new HashSet with the items that are in both sets.

        Raises:
            TypeError: if other is not a HashSet.
        """
        self._require_hashset(other)
        result = HashSet()
        other_table = other._table
        for item in self._table.keys():
            if other_table.contains(item):
                result._table.put(item, True)
        return result

    def difference(self, other):
        """Return a new HashSet with the items in this set but not in other.

        Raises:
            TypeError: if other is not a HashSet.
        """
        self._require_hashset(other)
        result = HashSet()
        other_table = other._table
        for item in self._table.keys():
            if not other_table.contains(item):
                result._table.put(item, True)
        return result

    def symmetric_difference(self, other):
        """Return a new HashSet with the items that are in exactly one set.

        Raises:
            TypeError: if other is not a HashSet.
        """
        self._require_hashset(other)
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
        """Return True if every item in this set is also in other.

        Raises:
            TypeError: if other is not a HashSet.
        """
        self._require_hashset(other)
        other_table = other._table
        for item in self._table.keys():
            if not other_table.contains(item):
                return False
        return True