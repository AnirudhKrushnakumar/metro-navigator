# Metro Navigator

**Name:** Anirudh Krushnakumar

**Class period:** Block 1 & 2A

## How to run it

From the repository root:

```
python main.py
python -m unittest discover -s tests -t .
```

`main.py` doesn't ask for any input. It prints eleven labeled sections, one for each part of the city system.

## The Eight Classes

### LinkedList (`linked_list.py`)

A singly linked list made of my own `Node` objects, with `head`, `tail`, and a size counter. In the demo it's the trip log. It's also what Stack, Queue, and Graph are built on.

```python
trip = LinkedList()
trip.append("Airport")
trip.append("Downtown")
trip.append("Campus")
print(trip)        # Airport -> Downtown -> Campus -> None
trip.reverse()
print(trip)        # Campus -> Downtown -> Airport -> None
```

**Design decision:** `reverse()` flips the existing `next` links instead of building a new list, and it moves `tail` to the old head so `append` still works afterward.

### HashTable (`hash_table.py`)

Stores key/value pairs with string keys. It starts with 8 buckets, and each bucket is a chain of my own `Entry` nodes (`key`, `value`, `next`). The hash function multiplies a running total by 31 and adds `ord()` of each character, so the order of the letters matters. In the demo it holds the fare zones.

```python
fares = HashTable()
fares.put("Beach", 3)
print(fares.get("Beach"))        # 3
print(fares.get("Nowhere", 0))   # 0
```

**Design decision:** only adding a new key can trigger a resize (when the load factor goes over 0.75). Updating a key that's already there never does.

### BST (`bst.py`)

A binary search tree made of `TreeNode` objects, for the alphabetical station directory. Keys are ints or strings (not mixed). It has all four traversals, `delete`, `range_query`, and `is_valid_bst`.

```python
stations = BST()
for name in ["Downtown", "Beach", "Factory", "Airport"]:
    stations.insert(name)
print(stations.inorder())   # ['Airport', 'Beach', 'Downtown', 'Factory']
```

**Design decision:** `insert`, `contains`, and `get` use loops instead of recursion. Inserting keys in sorted order makes a very tall tree, and a loop can't run out of recursion depth. When deleting a node with two children, I swap in the inorder successor (the smallest key on the right).

### MinHeap (`min_heap.py`)

An array-based min-heap. `_data` is a plain list of `(priority, item)` pairs, with the parent and child positions found by index math. In the demo it orders the maintenance tasks.

```python
tasks = MinHeap()
tasks.push(3, "Inspect Beach-Campus sign")
tasks.push(1, "Repair Eastside crossing")
print(tasks.pop())   # (1, 'Repair Eastside crossing')
```

**Design decision:** the heap only ever compares priorities, never the items. That means two tasks with the same priority never get compared, so the items can be anything, even dictionaries.

### Graph (`graph.py`)

An unweighted graph (undirected unless you pass `directed=True`). A `HashTable` maps each station name to a `LinkedList` of `Edge` objects, and an `Edge` only stores where it points. There are no weights anywhere.

```python
g = Graph()
for name in ["Airport", "Downtown", "Eastside"]:
    g.add_vertex(name)
g.add_edge("Airport", "Downtown")
g.add_edge("Airport", "Eastside")
print(g.neighbors("Airport"))   # ['Downtown', 'Eastside']
print(g.edge_count())           # 2
```

**Design decision:** in an undirected graph each connection is stored in both directions, but it's counted once in a separate edge counter. `remove_vertex` only visits the vertex’s actual neighbors in an undirected graph, instead of checking every vertex. A directed graph also has to scan for edges that point at it.

### Stack (`linked_stack.py`)

A last-in, first-out stack. It keeps a `LinkedList` in `_list` and uses the head of the list as the top. In the demo it's the rider's Back button. The file also has `is_balanced(text)`, which uses the Stack to check `()`, `[]`, and `{}`.

```python
back = Stack()
back.push("Airport")
back.push("Downtown")
print(back.pop())                # Downtown
print(is_balanced("([]{})"))     # True
print(is_balanced("([)]"))       # False
```

**Design decision:** the top is the head, so `push` and `pop` work on the front of the list and never walk it.

### Queue (`linked_queue.py`)

A first-in, first-out queue. It keeps a `LinkedList` in `_list`, with the front at the head and the back at the tail. In the demo it's the ticket line. The file also has `board_passengers(names, seats_available)`, which boards riders in order until the seats run out, and `hot_potato(namelist, num)`, the counting-out game.

```python
line = Queue()
line.enqueue("Ana")
line.enqueue("Ben")
print(line.dequeue())                                  # Ana
print(board_passengers(["Ava", "Ben", "Cy", "Dee"], 2))
# (['Ava', 'Ben'], ['Cy', 'Dee'])
print(hot_potato(["A", "B", "C", "D", "E"], 3))
# (['C', 'A', 'E', 'B'], 'D')
```

**Design decision:** `enqueue` uses the tail and `dequeue` uses the head, so neither one walks the list. `board_passengers` makes its own Queue from the names, so the list you pass in is never changed.

### HashSet (`hash_set.py`)

A set of unique strings. It keeps a `HashTable` in `_table`, with each item stored as a key. In the demo it compares which stations are neighbors of other stations.

```python
a = HashSet()
b = HashSet()
for name in ["Downtown", "Eastside"]:
    a.add(name)
for name in ["Downtown", "Garden"]:
    b.add(name)
print(a.intersection(b).to_list())   # ['Downtown']
print(len(a.union(b)))               # 3
```

**Design decision:** `union`, `intersection`, `difference`, and `symmetric_difference` all return a new HashSet, so the two original sets are never changed.

## Known Bugs

None that I know of. Every unit test passes, and `main.py` runs without errors.

One thing worth knowing: the project packet and the rubric describe `board_passengers` differently. The packet says it's the counting-out game, and the rubric says it's a boarding simulation with a seat count. I followed the rubric for `board_passengers` and kept the counting-out version as `hot_potato`, which is also the name the unit tests use.

## Unique Design Choice

`LinkedList` keeps a `tail` pointer. Without it, adding to the end would mean walking the whole list to find the last node. With it, `append` jumps straight there:

```python
def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self._size += 1
```

The Queue depends on this. Adding at the tail and removing at the head means neither end needs a walk.

## Reflection

The slowest bug to find was in `Graph.remove_vertex`. My first version checked every vertex for an edge to the one being removed, and the 1,000-vertex stress test ran too slowly. Switching it to only look at the vertex's neighbors fixed it. I also caught a couple of banned tools late, a built-in `hash()` in the HashTable and a dictionary inside `is_balanced`, and replaced them with my own hash function and plain strings. The last open question was the `board_passengers` mix-up described above.