class Entry:
    """One key/value pair in a bucket's chain."""

    def __init__(self, key, value, next_entry=None):
        """Create an entry that links to next_entry (or None)."""
        self.key = key
        self.value = value
        self.next = next_entry

class HashTable:
    """A hash table with string keys that uses separate chaining.

    The bucket count doubles whenever the load factor goes above 0.75.
    """

    def __init__(self, capacity=8):
        """Create an empty table with the given number of buckets (default 8)."""
        self.capacity = capacity
        self._size = 0
        self.buckets = [None] * capacity

    def _validate_key(self, key):
        """Raise TypeError if key is not a string."""
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}")

    def _hash(self, key):
        """Return the bucket index (0 to capacity - 1) for key.

        Raises:
            TypeError: if key is not a string.
        """
        self._validate_key(key)
        total = 0
        # multiplying by 31 makes a character's position matter, and the mod keeps it small
        for char in key:
            total = (total * 31 + ord(char)) % self.capacity
        return total

    def __len__(self):
        """Return the number of stored key/value pairs."""
        return self._size

    def is_empty(self):
        """Return True if the table holds no entries."""
        return self._size == 0

    def load_factor(self):
        """Return the number of entries divided by the number of buckets."""
        return self._size / self.capacity
    
    def _resize(self):
        """Double the number of buckets and put every entry back in."""
        # entries must be placed again because the bucket index depends on the capacity
        old_items = self.items()
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self._size = 0

        for k, v in old_items:
            self.put(k, v)
    
    def put(self, key, value):
        """Insert key, or update its value if the key already exists.

        Raises:
            TypeError: if key is not a string.
        """
        self._validate_key(key)
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # a new key goes at the front of its chain
        self.buckets[index] = Entry(key, value, self.buckets[index])
        self._size += 1
        # only a new key can trigger a resize, never an update
        if self.load_factor() > 0.75:
            self._resize()

    def get(self, key, default=None):
        """Return the value stored for key, or default if key is absent."""
        self._validate_key(key)
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return default

    def remove(self, key):
        """Remove key and return its value.

        Raises:
            KeyError: if key is not in the table.
        """
        self._validate_key(key)
        index = self._hash(key)
        current = self.buckets[index]
        prev = None

        while current is not None:
            if current.key == key:
                # prev is None when the entry is the head of its chain
                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next

                self._size -= 1
                return current.value

            prev = current
            current = current.next

        raise KeyError(f"Key not found for removal: {key}")

    def contains(self, key):
        """Return True if key is in the table."""
        self._validate_key(key)
        index = self._hash(key)
        current = self.buckets[index]
        while current is not None:
            if current.key == key:
                return True
            current = current.next
        return False

    def keys(self):
        """Return a list of all keys."""
        all_keys = []
        for bucket in self.buckets:
            current = bucket
            while current is not None:
                all_keys.append(current.key)
                current = current.next
        return all_keys

    def values(self):
        """Return a list of all values, in the same order as keys()."""
        all_values = []
        for bucket in self.buckets:
            current = bucket
            while current is not None:
                all_values.append(current.value)
                current = current.next
        return all_values

    def items(self):
        """Return a list of (key, value) tuples, in the same order as keys()."""
        all_items = []
        for bucket in self.buckets:
            current = bucket
            while current is not None:
                all_items.append((current.key, current.value))
                current = current.next
        return all_items

    def __contains__(self, key):
        """Support `key in table`."""
        return self.contains(key)

    def __setitem__(self, key, value):
        """Support `table[key] = value`."""
        self.put(key, value)

    def __getitem__(self, key):
        """Support `table[key]`.

        Raises:
            KeyError: if key is not in the table.
        """
        val = self.get(key, default=None)
        # None can be a stored value, so check the keys before raising
        if val is None and key not in self.keys():
            raise KeyError(f"Key not found: {key}")
        return val

    def clear(self):
        """Remove every entry and reset the capacity to 8."""
        self.capacity = 8
        self._size = 0
        self.buckets = [None] * self.capacity