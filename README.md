# City Transportation Network Using Graph Algorithms

## Project Overview
The City Transportation Network is a Python-based project that represents a city's transportation system using a graph data structure. In this project, locations such as railway stations, bus stands, hospitals, shopping malls, airports, and universities are represented as vertices, while roads connecting these locations are represented as weighted edges.

The project uses an adjacency list to represent the network and applies BFS, DFS, Kruskal's algorithm, and Dijkstra's algorithm to analyze connectivity, construct a minimum-cost road network, and find shortest routes between locations.

## Objectives
- To represent a city transportation network using an adjacency list.
- To implement Breadth-First Search (BFS) for connectivity analysis.
- To implement Depth-First Search (DFS) for graph traversal.
- To use Kruskal's algorithm to construct a Minimum Spanning Tree (MST).
- To implement Dijkstra's algorithm to find the shortest routes.
- To understand the practical applications of graph algorithms in transportation systems.

## Technologies Used
- Programming Language: Python
- Data Structure: Graph using an adjacency list
- Algorithms: BFS, DFS, Kruskal's Algorithm, and Dijkstra's Algorithm
- Platform: Python IDLE, Programiz Online Compiler, or any Python-supported IDE

## City Locations
The transportation network contains the following locations:

| Vertex | Location |
|---|---|
| A | Railway Station |
| B | Bus Stand |
| C | Hospital |
| D | Shopping Mall |
| E | Airport |
| F | University |

## Road Network
The following roads connect the locations. The weights represent distances in kilometers.

| Starting Location | Destination | Distance |
|---|---|---:|
| Railway Station | Bus Stand | 4 km |
| Railway Station | Hospital | 3 km |
| Bus Stand | Hospital | 2 km |
| Bus Stand | Shopping Mall | 5 km |
| Hospital | Shopping Mall | 3 km |
| Hospital | Airport | 6 km |
| Shopping Mall | Airport | 2 km |
| Shopping Mall | University | 4 km |
| Airport | University | 3 km |

## Algorithms Implemented

### 1. Breadth-First Search (BFS)
BFS traverses the graph level by level, visiting neighboring locations before moving to locations farther away. It helps explore the connectivity of the transportation network.

### 2. Depth-First Search (DFS)
DFS explores one path as deeply as possible before backtracking. It helps traverse the network and determine which locations are reachable from a starting location.

### 3
