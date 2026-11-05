from linked_list import LinkedList

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self._size = 0
        self.buckets = [LinkedList() for _ in range(capacity)]

    def _validate_key(self, key):
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}")

    def _hash(self, key):
        self._validate_key(key)
        return abs(hash(key)) % self.capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def load_factor(self):
        return self._size / self.capacity
    
    def _resize(self):
        old_items = self.items()
        self.capacity *= 2
        self.buckets = [LinkedList() for _ in range(self.capacity)]
        self._size = 0

        for k, v in old_items:
            self.put(k, v)
    
    def put(self, key, value):
        self._validate_key(key)
        index = self._hash(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current is not None:
            k, v = current.value
            if k == key:
                current.value = (key, value)
                return
            current = current.next

        bucket.append((key, value))
        self._size += 1
        if self.load_factor() > 0.75:
            self._resize()

    def get(self, key, default=None):
        self._validate_key(key)
        index = self._hash(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current is not None:
            k, v = current.value
            if k == key:
                return v
            current = current.next

        return default

    def remove(self, key):
        self._validate_key(key)
        index = self._hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        prev = None

        while current is not None:
            k, v = current.value
            if k == key:
                if prev is None:
                    bucket.head = current.next
                    if bucket.head is None:
                        bucket.tail = None
                else:
                    prev.next = current.next
                    if current.next is None:
                        bucket.tail = prev

                bucket._size -= 1
                self._size -= 1
                return v

            prev = current
            current = current.next

        raise KeyError(f"Key not found for removal: {key}")

    def contains(self, key):
        self._validate_key(key)
        return self.get(key, default=None) is not None or key in self.keys()

    def keys(self):
        all_keys = []
        for bucket in self.buckets:
            current = bucket.head
            while current is not None:
                k, v = current.value
                all_keys.append(k)
                current = current.next
        return all_keys

    def values(self):
        all_values = []
        for bucket in self.buckets:
            current = bucket.head
            while current is not None:
                k, v = current.value
                all_values.append(v)
                current = current.next
        return all_values

    def items(self):
        all_items = []
        for bucket in self.buckets:
            current = bucket.head
            while current is not None:
                all_items.append(current.value)
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