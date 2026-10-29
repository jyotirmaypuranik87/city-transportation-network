from collections import deque
import heapq

# CITY TRANSPORTATION NETWORK
# A = Railway Station
# B = Bus Stand
# C = Hospital
# D = Shopping Mall
# E = Airport
# F = University

# Adjacency List: (Connected Location, Distance in km)

graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 3), ('B', 2), ('D', 3), ('E', 6)],
    'D': [('B', 5), ('C', 3), ('E', 2), ('F', 4)],
    'E': [('C', 6), ('D', 2), ('F', 3)],
    'F': [('D', 4), ('E', 3)]
}

locations = {
    'A': 'Railway Station',
    'B': 'Bus Stand',
    'C': 'Hospital',
    'D': 'Shopping Mall',
    'E': 'Airport',
    'F': 'University'
}


# 1. BREADTH-FIRST SEARCH (BFS)

def bfs(start):
    visited = set([start])
    queue = deque([start])
    traversal = []

    while queue:
        current = queue.popleft()
        traversal.append(current)

        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


# 2. DEPTH-FIRST SEARCH (DFS)

def dfs(start):
    visited = set()
    traversal = []

    def visit(current):
        visited.add(current)
        traversal.append(current)

        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return traversal


# 3. KRUSKAL'S ALGORITHM

def kruskal():
    edges = []

    for u in graph:
        for v, weight in graph[u]:
            if u < v:
                edges.append((weight, u, v))

    edges.sort()

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if root_u == root_v:
            return False

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

        return True

    mst = []
    total_distance = 0

    for weight, u, v in edges:
        if union(u, v):
            mst.append((u, v, weight))
            total_distance += weight

            if len(mst) == len(graph) - 1:
                break

    if len(mst) != len(graph) - 1:
        return [], 0

    return mst, total_distance


# 4. DIJKSTRA'S SHORTEST PATH ALGORITHM

def dijkstra(start):
    distances = {
        node: float('inf')
        for node in graph
    }

    previous = {
        node: None
        for node in graph
    }

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_distance != distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


# FIND SHORTEST ROUTE

def get_route(start, destination, previous):
    route = []
    current = destination

    while current is not None:
        route.append(current)
        current = previous[current]

    route.reverse()

    if not route or route[0] != start:
        return "No route available"

    return " -> ".join(route)


# DISPLAY CITY LOCATIONS

def display_locations():
    print("\nCITY LOCATIONS")

    for code, name in locations.items():
        print(code, ":", name)


# DISPLAY ADJACENCY LIST

def display_graph():
    print("\nADJACENCY LIST")

    for node, neighbors in graph.items():
        print(node, ":", end=" ")

        connections = []

        for neighbor, distance in neighbors:
            connections.append(
                "{} ({} km)".format(neighbor, distance)
            )

        print(", ".join(connections))


# MAIN PROGRAM

def main():
    print("=" * 50)
    print("CITY TRANSPORTATION NETWORK")
    print("=" * 50)

    display_locations()
    display_graph()

    # BFS
    print("\n1. BREADTH-FIRST SEARCH (BFS)")

    bfs_result = bfs('A')

    print("Traversal:", " -> ".join(bfs_result))
    print("Total locations visited:", len(bfs_result))

    if len(bfs_result) == len(graph):
        print("Result: All locations are connected.")
    else:
        print("Result: Some locations are disconnected.")

    # DFS
    print("\n2. DEPTH-FIRST SEARCH (DFS)")

    dfs_result = dfs('A')

    print("Traversal:", " -> ".join(dfs_result))
    print("Total locations visited:", len(dfs_result))

    if len(dfs_result) == len(graph):
        print("Result: All locations are connected.")
    else:
        print("Result: Some locations are disconnected.")

    # Kruskal's Algorithm
    print("\n3. KRUSKAL'S ALGORITHM")
    print("Minimum Spanning Tree:")

    mst, total_distance = kruskal()

    if mst:
        for u, v, weight in mst:
            print(
                "{} - {} : {} km".format(
                    locations[u],
                    locations[v],
                    weight
                )
            )

        print("Total minimum road distance:", total_distance, "km")
        print("Number of roads selected:", len(mst))
    else:
        print("The network is disconnected.")

    # Dijkstra's Algorithm
    print("\n4. DIJKSTRA'S ALGORITHM")

    start = 'A'

    distances, previous = dijkstra(start)

    print("Starting location:", locations[start])

    for destination in graph:
        print("\nDestination:", locations[destination])

        if distances[destination] == float('inf'):
            print("Shortest distance: Unreachable")
            print("Route: No route available")
        else:
            print(
                "Shortest distance:",
                distances[destination],
                "km"
            )

            print(
                "Shortest route:",
                get_route(start, destination, previous)
            )

    print("\n" + "=" * 50)
    print("PROGRAM EXECUTED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()
