from graph import Graph
from bst import BST
from hash_table import HashTable
from linked_list import LinkedList

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

fare_zones = [
    ("Airport", 1),
    ("Beach", 3),
    ("Campus", 2),
    ("Downtown", 1),
    ("Eastside", 2),
    ("Factory", 2),
    ("Garden", 3),
]

trip_stops = ["Airport", "Downtown", "Campus", "Beach"]

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

def build_fare_table():
    fares = HashTable()
    for station, zone in fare_zones:
        fares.put(station, zone)
    return fares

def build_trip_log():
    trip_log = LinkedList()
    for stop in trip_stops:
        trip_log.append(stop)
    return trip_log





def main():
    graph = build_metro_graph()
    directory = build_station_directory()
    fares = build_fare_table()
    trip_log = build_trip_log()

    print_section("1. Metro City Map (Unweighted Graph)")
    print(graph)
    print(f"Stations: {graph.vertex_count()}    Connections: {graph.edge_count()}")

    print_section("2. Station Directory (BST)")
    print(f"Alphabetical (inorder): {directory.inorder()}")
    print(f"Level by level:         {directory.level_order()}")
    print(f"Preorder:               {directory.preorder()}")
    print(f"Height: {directory.height()}  Leaves: {directory.count_leaves()}")

    print_section("3. Fare Zones (HashTable)")
    for station in directory.inorder():
        print(f"{station:<10} -> Zone {fares.get(station)}")
    print(f"Stations in fare table: {len(fares)}")

    print_section("4. Trip Log (LinkedList)")
    print(f"Forward:    {trip_log}")
    trip_log.reverse()
    print(f"Reversed:   {trip_log}")





if __name__ == "__main__":
    main()