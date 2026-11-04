from linked_list import LinkedList

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self._size = 0
        self.buckets = [LinkedList() for _ in range(capacity)]

    def _hash(self, key):
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
        index = self._hash(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current is not None:
            k, v = current.value
            if k == key:
                current.value = (key, value)
                return
            current = current.next

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current is not None:
            k, v = current.value
            if k == key:
                return v
            current = current.next

        raise KeyError(f"Key not found: {key}")

    def remove(self, key):
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

        raise KeyError(f"Key not found for removal: {key}")

    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

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
                all_items.append(current.values)
                current = current.next

        return all_items

    def __contains__(self, key):
            return self.contains(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)