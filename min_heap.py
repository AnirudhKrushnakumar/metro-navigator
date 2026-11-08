class MinHeap:
    """An array-based min-heap of (priority, item) pairs.

    Only the priority is compared, so items can be any type.
    """

    def __init__(self):
        """Create an empty heap."""
        self._data = []
        self._size = 0

    def __len__(self):
        """Return the number of pairs in the heap."""
        return self._size

    def is_empty(self):
        """Return True if the heap has no pairs."""
        return self._size == 0

    def to_list(self):
        """Return a copy of the internal array, so changing it will not change the heap."""
        return list(self._data)

    def peek_min(self):
        """Return the pair with the smallest priority without removing it.

        Raises:
            IndexError: if the heap is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty heap")
        return self._data[0]

    def peek(self):
        """Return the pair with the smallest priority without removing it (see peek_min)."""
        return self.peek_min()

    def _parent(self, i):
        """Return the index of the parent of index i."""
        return (i - 1) // 2

    def _left_child(self, i):
        """Return the index of the left child of index i."""
        return 2 * i + 1

    def _right_child(self, i):
        """Return the index of the right child of index i."""
        return 2 * i + 2

    def _percolate_up(self, i):
        """Move the pair at index i up until its parent's priority is not larger."""
        while i > 0:
            p = self._parent(i)
            if self._data[i][0] < self._data[p][0]:
                self._data[i], self._data[p] = self._data[p], self._data[i]
                i = p
            else:
                break

    def _percolate_down(self, i):
        """Move the pair at index i down, swapping with the smaller child."""
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
        """Add a (priority, item) pair and restore the heap order.

        Raises:
            TypeError: if priority is not an int or a float.
        """
        if isinstance(key, bool) or not isinstance(key, (int, float)):
            raise TypeError("Priority must be an int or float")
        self._data.append((key, value))
        self._size += 1
        self._percolate_up(len(self._data) - 1)

    def push(self, key, value=None):
        """Add a (priority, item) pair (see insert)."""
        self.insert(key, value)

    def extract_min(self):
        """Remove and return the pair with the smallest priority.

        Raises:
            IndexError: if the heap is empty.
        """
        if self.is_empty():
            raise IndexError("Extract from empty heap")

        root = self._data[0]
        last = self._data.pop()
        self._size -= 1

        if not self.is_empty():
            # the last pair takes the root's place, then sifts down
            self._data[0] = last
            self._percolate_down(0)

        return root

    def pop(self):
        """Remove and return the pair with the smallest priority (see extract_min).

        Raises:
            IndexError: if the heap is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty heap")
        return self.extract_min()

    def drain(self):
        """Remove every pair and return them in ascending priority order."""
        items = []
        while not self.is_empty():
            items.append(self.extract_min())
        return items

    def is_valid_heap(self):
        """Return True if every parent's priority is <= each of its children's."""
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

    def build_heap(items):
        """Return a NEW heap built bottom-up from (priority, item) pairs.

        The input list is not modified.

        Raises:
            TypeError: if a priority is not an int or a float.
        """
        h = MinHeap()
        for item in items:
            k, v = item
            if isinstance(k, bool) or not isinstance(k, (int, float)):
                raise TypeError("Priority must be an int or float")
            h._data.append((k, v))
            h._size += 1

        # bottom-up: start at the last parent and sift each one down
        for i in range(len(h._data) // 2 - 1, -1, -1):
            h._percolate_down(i)
        return h

    build_heap = staticmethod(build_heap)