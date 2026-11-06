from hash_table import HashTable

class Graph:
    def __init__(self):
        self.adjacency_list = HashTable()
        self.list = self.adjacency_list
        self._list = self.adjacency_list

    def add_vertex(self, vertex):
        if not self.self.adjacency_list.contains(vertex):
            self.adjacency_list.put(vertex, HashTable())

    def add_edge(self, v1, v2, weight=1):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adjacency_list.get(v1).put(v2, weight)
        self.adjacency_list.get(v2).put(v1, weight)

    def get_vertices(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        if self.adjacency_list.contains(vertex):
            return self.adjacency_list.get(vertex).keys()
        return []

    def get_weight(self, v1, v2):
        if self.adjacency_list.contains(v1):
            neighbors = self.adjacency_list.get(v1)
            if neighbors.contains(v2):
                return neighbors.get(v2)
        return None