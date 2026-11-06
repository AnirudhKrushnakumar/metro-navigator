class Entry:
    def __init__(self, key, value, next_entry=None):
        self.key = key
        self.value = value
        self.next = next_entry

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self._size = 0
        self.buckets = [None] * capacity

    def _validate_key(self, key):
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}")

    def _hash(self, key):
        self._validate_key(key)
        total = 0
        for char in key:
            total = (total * 31 + ord(char)) % self.capacity
        return total

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def load_factor(self):
        return self._size / self.capacity
    
    def _resize(self):
        old_items = self.items()
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self._size = 0

        for k, v in old_items:
            self.put(k, v)
    
    def put(self, key, value):
        self._validate_key(key)
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        self.buckets[index] = Entry(key, value, self.buckets[index])
        self._size += 1
        if self.load_factor() > 0.75:
            self._resize()

    def get(self, key, default=None):
        self._validate_key(key)
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return default

    def remove(self, key):
        self._validate_key(key)
        index = self._hash(key)
        current = self.buckets[index]
        prev = None

        while current is not None:
            if current.key == key:
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
        self._validate_key(key)
        index = self._hash(key)
        current = self.buckets[index]
        while current is not None:
            if current.key == key:
                return True
            current = current.next
        return False

    def keys(self):
        all_keys = []
        for bucket in self.buckets:
            current = bucket
            while current is not None:
                all_keys.append(current.key)
                current = current.next
        return all_keys

    def values(self):
        all_values = []
        for bucket in self.buckets:
            current = bucket
            while current is not None:
                all_values.append(current.value)
                current = current.next
        return all_values

    def items(self):
        all_items = []
        for bucket in self.buckets:
            current = bucket
            while current is not None:
                all_items.append((current.key, current.value))
                current = current.next
        return all_items

    def __contains__(self, key):
        return self.contains(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        val = self.get(key, default=None)
        if val is None and key not in self.keys():
            raise KeyError(f"Key not found: {key}")
        return val

    def clear(self):
        self.capacity = 8
        self._size = 0
        self.buckets = [None] * self.capacity