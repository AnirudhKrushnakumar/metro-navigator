class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def peek_min(self):
        if self.is_empty():
            return None
        return self.heap[0]
    
    def _parent(self, i):
        return (i - 1) // 2
    
    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2
    
    def _percolate_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self.heap[i] < self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.head[i]
                i = p
            else:
                break

    def _percolate_down(self, i):
        last_index = len(self.heap) - 1
        while self._left_child(i) <= last_index:
            left = self._left_child(i)
            right = self._right_child(i)
            smallest = i

            if self.heap[left] < self.heap[smallest]:
                smallest = left

            if right <= last_index and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break