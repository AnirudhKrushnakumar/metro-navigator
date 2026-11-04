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

    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __contains__(self, key):
        return self.contains(key)

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