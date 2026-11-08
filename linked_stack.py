from linked_list import LinkedList


class Stack:
    """A last-in, first-out stack. The top of the stack is the head of a LinkedList."""

    def __init__(self):
        """Create an empty stack."""
        self._list = LinkedList()

    def __len__(self):
        """Return the number of items on the stack."""
        return len(self._list)

    def is_empty(self):
        """Return True if the stack has no items."""
        return self._list.is_empty()

    def clear(self):
        """Remove every item from the stack."""
        self._list.clear()

    def to_list(self):
        """Return a new list of the items, top first."""
        return self._list.to_list()

    def push(self, item):
        """Put item on top of the stack."""
        self._list.prepend(item)

    def pop(self):
        """Remove and return the top item.

        Raises:
            IndexError: if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self._list.head.value
        self._list.remove_at(0)
        return item

    def peek(self):
        """Return the top item without removing it.

        Raises:
            IndexError: if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._list.head.value


def is_balanced(text):
    """Return True if every (, [ and { is closed by the matching type in order.

    All other characters are ignored.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string")

    stack = Stack()
    openers = "([{"
    closers = ")]}"

    for char in text:
        if char in openers:
            stack.push(char)
        elif char in closers:
            if stack.is_empty():
                return False
            top = stack.pop()
            # each closer must match the opener on top of the stack
            if openers.index(top) != closers.index(char):
                return False

    return stack.is_empty()