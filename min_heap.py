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