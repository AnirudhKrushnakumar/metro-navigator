from linked_list import LinkedList

class Stack:
    def __init__(self):
        self._list = LinkedList()

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return self._list.is_empty()

    def clear(self):
        self._list.clear()

    def to_list(self):
        return self._list.to_list()

    def push(self, item):
        self._list.prepend(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self._list.head.value
        self._list.remove_at(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._list.head.value

def is_balanced(text):
    if not isinstance(text, str):
        raise TypeError("Text must be a string")

    stack = Stack()
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in text:
            if char in "([{":
                stack.push(char)
            elif char in ")]}":
                if stack.is_empty():
                    return False
                top = stack.pop()
                if top != mapping[char]:
                    return False

    return stack.is_empty()