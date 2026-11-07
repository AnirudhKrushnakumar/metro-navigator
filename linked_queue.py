from linked_list import LinkedList

class Queue:
    """A first-in, first-out queue built on a LinkedList (front is the head, back is the tail)."""

    def __init__(self):
        """Create an empty queue."""
        self._list = LinkedList()

    def __len__(self):
        """Return the number of items in the queue."""
        return len(self._list)

    def is_empty(self):
        """Return True if the queue has no items."""
        return self._list.is_empty()

    def clear(self):
        """Remove every item from the queue."""
        self._list.clear()

    def to_list(self):
        """Return a new list of the items, front first."""
        return self._list.to_list()

    def enqueue(self, item):
        """Add item to the back of the queue."""
        self._list.append(item)

    def dequeue(self):
        """Remove and return the front item.

        Raises:
            IndexError: if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self._list.head.value
        self._list.remove_at(0)
        return item

    def peek(self):
        """Return the front item without removing it.

        Raises:
            IndexError: if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._list.head.value

def board_passengers(names, seats_available):
    """Board riders in arrival order until the seats run out.

    Returns:
        A tuple (boarded, still_waiting). The names list is not modified.

    Raises:
        TypeError: if seats_available is not an int, names is not a list or tuple,
            or a name is not a string.
        ValueError: if seats_available is negative.
    """
    if not isinstance(seats_available, int) or isinstance(seats_available, bool):
        raise TypeError("Seats available must be an integer")
    if seats_available < 0:
        raise ValueError("Seats available can't be negative")
    if not isinstance(names, (list, tuple)):
        raise TypeError("Names must be a list or tuple")

    queue = Queue()
    for name in names:
        if not isinstance(name, str):
            raise TypeError("Passenger names must be strings")
        queue.enqueue(name)

    boarded = []
    while not queue.is_empty() and len(boarded) < seats_available:
        boarded.append(queue.dequeue())

    waiting = queue.to_list()
    return boarded, waiting

# Guide Version
# 1. Delete the rubric board_passengers function above.
# 2. Uncomment the two lines below.
# def board_passengers(names, k):
#     return hot_potato(names, k)

def hot_potato(namelist, num):
    """Play the counting-out game on a queue of names.

    Starting at the front, num - 1 people move to the back and the next one is
    eliminated. This repeats until one person is left.

    Returns:
        A tuple (elimination_order, winner).

    Raises:
        ValueError: if namelist is empty or num is less than 1.
    """
    if not isinstance(namelist, (list, tuple)) or not namelist:
        raise ValueError("Namelist must be a non-empty list or tuple")
    if not isinstance(num, int) or isinstance(num, bool) or num < 1:
        raise ValueError("Num must be an integer greater than or equal to 1")
    
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    eliminated = []
    while len(queue) > 1:
        # the first num - 1 people go to the back, then the next one is eliminated
        for _ in range(num - 1):
            queue.enqueue(queue.dequeue())
        eliminated.append(queue.dequeue())

    winner = queue.dequeue() if not queue.is_empty() else None
    return eliminated, winner