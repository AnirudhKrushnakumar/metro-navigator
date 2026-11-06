from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def __len__(self):
        return len(self.list)

    def is_empty(self):
        return self.list.is_empty()

    def clear(self):
        self.list.clear()

    def to_list(self):
        return self.list.to_list()