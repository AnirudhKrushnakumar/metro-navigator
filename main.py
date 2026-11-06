from graph import Graph

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

def main():
    graph = build_metro_graph()

    print_section("1. Metro City Map (Unweighted Graph)")
    print(graph)
    print(f"Stations: {graph.vertex_count()}    Connections: {graph.edge_count()}")





if __name__ == "__main__":
    main()