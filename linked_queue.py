from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()
        self._list = self.list

    def __len__(self):
        return len(self.list)

    def is_empty(self):
        return self.list.is_empty()

    def clear(self):
        self.list.clear()

    def to_list(self):
        return self.list.to_list()