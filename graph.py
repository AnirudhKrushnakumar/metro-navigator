from hash_table import HashTable
from linked_list import LinkedList


class Edge:
    """A connection to another vertex (it stores only the vertex it points to)."""

    def __init__(self, to):
        """Create an edge pointing to the vertex named to."""
        self.to = to


class Graph:
    """An unweighted graph (undirected by default).

    A HashTable maps each vertex name to a LinkedList of Edge objects.
    """

    def __init__(self, directed=False):
        """Create an empty graph; pass directed=True for a directed graph."""
        self.directed = directed
        self._adj = HashTable()
        self._edge_count = 0

    def vertex_count(self):
        """Return the number of vertices."""
        return len(self._adj)

    def edge_count(self):
        """Return the number of connections (an undirected one counts once)."""
        return self._edge_count

    def vertices(self):
        """Return a list of all vertex names (any order)."""
        return self._adj.keys()

    def has_vertex(self, name):
        """Return True if name is a vertex in the graph."""
        return isinstance(name, str) and self._adj.contains(name)

    def _require_vertex(self, name):
        """Raise KeyError if name is not a vertex."""
        if not self.has_vertex(name):
            raise KeyError(f"Vertex not found: {name}")

    def _edge_index(self, u, v):
        """Return the position of the edge u -> v in u's edge list, or -1."""
        index = 0
        current = self._adj.get(u).head
        while current is not None:
            if current.value.to == v:
                return index
            current = current.next
            index += 1
        return -1

    def add_vertex(self, name):
        """Add a vertex.

        Returns:
            True if it was added, False if it was already there.

        Raises:
            TypeError: if name is not a string.
            ValueError: if name is an empty string.
        """
        if not isinstance(name, str):
            raise TypeError("Vertex name must be a string")
        if name == "":
            raise ValueError("Vertex name cannot be empty")
        if self._adj.contains(name):
            return False
        self._adj.put(name, LinkedList())
        return True

    def add_edge(self, u, v):
        """Connect vertices u and v.

        Returns:
            True if a new connection was added, False if it already existed.

        Raises:
            KeyError: if either vertex does not exist.
            ValueError: if u and v are the same vertex.
        """
        self._require_vertex(u)
        self._require_vertex(v)
        if u == v:
            raise ValueError("Self-loops are not allowed")
        if self._edge_index(u, v) != -1:
            return False
        self._adj.get(u).append(Edge(v))
        # undirected: store the connection in both directions but count it once
        if not self.directed:
            self._adj.get(v).append(Edge(u))
        self._edge_count += 1
        return True

    def has_edge(self, u, v):
        """Return True if u -> v exists (False if either vertex is missing)."""
        if not self.has_vertex(u) or not self.has_vertex(v):
            return False
        return self._edge_index(u, v) != -1

    def remove_edge(self, u, v):
        """Remove the connection between u and v.

        Returns:
            True if it was removed, False if there was no such edge.

        Raises:
            KeyError: if either vertex does not exist.
        """
        self._require_vertex(u)
        self._require_vertex(v)
        index = self._edge_index(u, v)
        if index == -1:
            return False
        self._adj.get(u).remove_at(index)
        # undirected: remove the reverse direction too
        if not self.directed:
            self._adj.get(v).remove_at(self._edge_index(v, u))
        self._edge_count -= 1
        return True

    def remove_vertex(self, name):
        """Remove a vertex and every edge that touches it.

        Returns:
            True if it was removed, False if the vertex was not in the graph.
        """
        if not self.has_vertex(name):
            return False
        for other in self.neighbors(name):
            self.remove_edge(name, other)
        # in a directed graph other vertices can point at name, so look for incoming edges
        if self.directed:
            for other in self._adj.keys():
                if self.has_edge(other, name):
                    self.remove_edge(other, name)
        self._adj.remove(name)
        return True

    def neighbors(self, name):
        """Return a new list of the neighbors of name, in the order they were added.

        Raises:
            KeyError: if the vertex does not exist.
        """
        self._require_vertex(name)
        return [edge.to for edge in self._adj.get(name)]

    def degree(self, name):
        """Return the number of outgoing edges from name.

        Raises:
            KeyError: if the vertex does not exist.
        """
        self._require_vertex(name)
        return len(self._adj.get(name))

    def edges(self):
        """Return a list of (u, v) pairs.

        An undirected connection is listed once with u < v.
        """
        result = []
        for u in self._adj.keys():
            for v in self.neighbors(u):
                # an undirected connection is stored twice, so list it only when u < v
                if self.directed or u < v:
                    result.append((u, v))
        return result

    def __str__(self):
        """Return an adjacency listing with one vertex per line."""
        lines = []
        for v in self._adj.keys():
            lines.append(f"{v}: {', '.join(self.neighbors(v))}")
        return "\n".join(lines)