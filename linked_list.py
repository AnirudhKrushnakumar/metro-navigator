class Node:
    """A single node in a singly linked list."""

    def __init__(self, value, next_node=None):
        """Create a node holding value that points to next_node (or None)."""
        self.value = value
        self.next = next_node


class LinkedList:
    """A singly linked list that keeps track of its own head, tail and size."""

    def __init__(self):
        """Create an empty list (head and tail are both None)."""
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Return the number of values stored."""
        return self._size

    def is_empty(self):
        """Return True if the list holds no values."""
        return self._size == 0

    def append(self, value):
        """Add value to the end. Uses the tail, so the list is never walked."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        """Add value to the front of the list."""
        new_node = Node(value, next_node=self.head)
        self.head = new_node

        # the first node added to an empty list is also the tail
        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def _get_node(self, index):
        """Return the node at index (the caller must check the index first)."""
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def get(self, index):
        """Return the value at index.

        Raises:
            IndexError: if index is negative or not less than the length.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")

        target_node = self._get_node(index)
        return target_node.value

    def remove_at(self, index):
        """Remove the node at index and return its value.

        Removing index 0 takes the head directly without walking the list.

        Raises:
            IndexError: if index is negative or not less than the length.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")
        assert self.head is not None

        if index == 0:
            removed_val = self.head.value
            self.head = self.head.next
            self._size -= 1

            # the list is now empty, so the tail must be cleared too
            if self.is_empty():
                self.tail = None

            return removed_val

        prev = self._get_node(index - 1)
        target = prev.next
        assert target is not None

        removed_val = target.value
        prev.next = target.next

        # removing the last node means the tail moves back to the previous node
        if index == self._size - 1:
            self.tail = prev

        self._size -= 1
        return removed_val

    def remove(self, value):
        """Remove the first node equal to value.

        Returns:
            True if a node was removed, False if value was not found.
        """
        idx = self.find(value)
        if idx == -1:
            return False
        self.remove_at(idx)
        return True

    def to_list(self):
        """Return a new Python list of the values from head to tail."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def find(self, value):
        """Return the index of the first node equal to value, or -1 if not found."""
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        """Reverse the list in place by flipping each next link (no new nodes)."""
        prev = None
        current = self.head
        # the old head becomes the new tail
        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def __iter__(self):
        """Yield the values from head to tail."""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def insert_at(self, index, value):
        """Insert value so that it ends up at index.

        Raises:
            IndexError: unless 0 <= index <= len(self).
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(value)
            return

        if index == self._size:
            self.append(value)
            return

        prev = self._get_node(index - 1)
        new_node = Node(value, next_node=prev.next)
        prev.next = new_node
        self._size += 1

    def clear(self):
        """Remove every value from the list."""
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        """Return the values joined by arrows, like '1 -> 2 -> None' ('None' if empty)."""
        if self.is_empty():
            return "None"

        result = ""
        current = self.head
        while current is not None:
            result += str(current.value) + " -> "
            current = current.next
        return result + "None"