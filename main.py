from graph import Graph
from bst import BST

stations = ["Downtown", "Beach", "Factory", "Airport", "Campus", "Eastside", "Garden"]

connections = [
    ("Airport", "Downtown"),
    ("Airport", "Eastside"),
    ("Beach", "Campus"),
    ("Beach", "Garden"),
    ("Campus", "Downtown"),
    ("Downtown", "Eastside"),
    ("Downtown", "Factory"),
    ("Eastside", "Factory"),
    ("Factory", "Garden"),
]

def print_section(title):
    print()
    print("=-=" * 17)
    print(title)
    print("=-=" * 17)

def build_metro_graph():
    graph = Graph()
    for station in stations:
        graph.add_vertex(station)
    for station_a, station_b in connections:
        graph.add_edge(station_a, station_b)
    return graph

def build_station_directory():
    directory = BST()
    for station in stations:
        directory.insert(station)
    return directory

def main():
    graph = build_metro_graph()
    directory = build_station_directory()

    print_section("1. Metro City Map (Unweighted Graph)")
    print(graph)
    print(f"Stations: {graph.vertex_count()}    Connections: {graph.edge_count()}")

    print_section("2. Station Directory (BST)")
    print(f"Alphabetical (inorder): {directory.inorder()}")
    print(f"Level by level:         {directory.level_order()}")
    print(f"Preorder:               {directory.preorder()}")
    print(f"Height: {directory.height()}  Leaves: {directory.count_leaves()}")





if __name__ == "__main__":
    main()