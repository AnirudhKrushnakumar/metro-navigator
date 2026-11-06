from hash_table import HashTable
from linked_list import LinkedList


class Edge:
    def __init__(self, to):
        self.to = to


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self._adj = HashTable()
        self._edge_count = 0

    def vertex_count(self):
        return len(self._adj)

    def edge_count(self):
        return self._edge_count

    def vertices(self):
        return self._adj.keys()

    def has_vertex(self, name):
        return isinstance(name, str) and self._adj.contains(name)

    def _require_vertex(self, name):
        if not self.has_vertex(name):
            raise KeyError(f"Vertex not found: {name}")

    def _edge_index(self, u, v):
        index = 0
        current = self._adj.get(u).head
        while current is not None:
            if current.value.to == v:
                return index
            current = current.next
            index += 1
        return -1

    def add_vertex(self, name):
        if not isinstance(name, str):
            raise TypeError("Vertex name must be a string")
        if name == "":
            raise ValueError("Vertex name cannot be empty")
        if self._adj.contains(name):
            return False
        self._adj.put(name, LinkedList())
        return True

    def add_edge(self, u, v):
        self._require_vertex(u)
        self._require_vertex(v)
        if u == v:
            raise ValueError("Self-loops are not allowed")
        if self._edge_index(u, v) != -1:
            return False
        self._adj.get(u).append(Edge(v))
        if not self.directed:
            self._adj.get(v).append(Edge(u))
        self._edge_count += 1
        return True

    def has_edge(self, u, v):
        if not self.has_vertex(u) or not self.has_vertex(v):
            return False
        return self._edge_index(u, v) != -1

    def remove_edge(self, u, v):
        self._require_vertex(u)
        self._require_vertex(v)
        index = self._edge_index(u, v)
        if index == -1:
            return False
        self._adj.get(u).remove_at(index)
        if not self.directed:
            self._adj.get(v).remove_at(self._edge_index(v, u))
        self._edge_count -= 1
        return True

    def remove_vertex(self, name):
        if not self.has_vertex(name):
            return False
        for other in self._adj.keys():
            if other == name:
                continue
            self.remove_edge(name, other)
            self.remove_edge(other, name)
        self._adj.remove(name)
        return True

    def neighbors(self, name):
        self._require_vertex(name)
        return [edge.to for edge in self._adj.get(name)]

    def degree(self, name):
        self._require_vertex(name)
        return len(self._adj.get(name))

    def edges(self):
        result = []
        for u in self._adj.keys():
            for v in self.neighbors(u):
                if self.directed or u < v:
                    result.append((u, v))
        return result

    def __str__(self):
        lines = []
        for v in self._adj.keys():
            lines.append(f"{v}: {', '.join(self.neighbors(v))}")
        return "\n".join(lines)