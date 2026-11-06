class MinHeap:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def to_list(self):
        return list(self._data)

    def peek_min(self):
        if self.is_empty():
            raise IndexError("Peek from empty heap")
        return self._data[0]

    def peek(self):
        return self.peek_min()

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _percolate_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self._data[i][0] < self._data[p][0]:
                self._data[i], self._data[p] = self._data[p], self._data[i]
                i = p
            else:
                break

    def _percolate_down(self, i):
        last_index = len(self._data) - 1
        while self._left_child(i) <= last_index:
            left = self._left_child(i)
            right = self._right_child(i)
            smallest = i

            if self._data[left][0] < self._data[smallest][0]:
                smallest = left

            if right <= last_index and self._data[right][0] < self._data[smallest][0]:
                smallest = right

            if smallest != i:
                self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
                i = smallest
            else:
                break

    def insert(self, key, value=None):
        if isinstance(key, bool) or not isinstance(key, (int, float)):
            raise TypeError("Priority must be an int or float")
        self._data.append((key, value))
        self._percolate_up(len(self._data) - 1)

    def push(self, key, value=None):
        self.insert(key, value)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Extract from empty heap")

        root = self._data[0]
        last = self._data.pop()

        if not self.is_empty():
            self._data[0] = last
            self._percolate_down(0)

        return root

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty heap")
        return self.extract_min()

    def drain(self):
        items = []
        while not self.is_empty():
            items.append(self.extract_min())
        return items

    def is_valid_heap(self):
        n = len(self._data)
        for i in range(n):
            left = self._left_child(i)
            right = self._right_child(i)
            try:
                if left < n and self._data[left][0] < self._data[i][0]:
                    return False
                if right < n and self._data[right][0] < self._data[i][0]:
                    return False
            except Exception:
                return False
        return True

    @staticmethod
    def build_heap(items):
        h = MinHeap()
        for item in items:
            k, v = item
            if isinstance(k, bool) or not isinstance(k, (int, float)):
                raise TypeError("Priority must be an int or float")
            h._data.append((k, v))

        for i in range(len(h._data) // 2 - 1, -1, -1):
            h._percolate_down(i)
        return h