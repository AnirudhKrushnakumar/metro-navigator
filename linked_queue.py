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

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.list.head.value
        self.list.remove_at(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.list.head.value

def board_passengers(names, seats_available):
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

def hot_potato(namelist, num):
    if not isinstance(namelist, (list, tuple)) or not namelist:
        raise ValueError("Namelist must be a non-empty list or tuple")
    if not isinstance(num, int) or isinstance(num, bool) or num < 1:
        raise ValueError("Num must be an integer greater than or equal to 1")
    
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    eliminated = []
    while len(queue) > 1:
        for _ in range(num - 1):
            queue.enqueue(queue.dequeue())
        eliminated.append(queue.dequeue())

    winner = queue.dequeue() if not queue.is_empty() else None
    return eliminated, winner