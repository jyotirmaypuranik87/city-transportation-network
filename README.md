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

### 3. Kruskal's Algorithm
Kruskal's algorithm finds a Minimum Spanning Tree (MST) by selecting the lowest-weight edges without forming cycles. It identifies a set of roads that connects all locations with minimum total distance.

**Expected MST total distance: 13 km.**

### 4. Dijkstra's Algorithm
Dijkstra's algorithm calculates the shortest distance from a starting location to every other reachable location in a weighted graph with non-negative edge weights.

It helps determine efficient routes between important city locations.

## Expected Results
When the program runs, it demonstrates:
- BFS traversal of the transportation network.
- DFS traversal of the transportation network.
- Minimum Spanning Tree generated using Kruskal's algorithm.
- Minimum total distance required to connect all locations.
- Shortest distances and routes from the Railway Station to other locations.

### Expected Shortest Distances from Railway Station

| Destination | Shortest Distance |
|---|---:|
| Railway Station | 0 km |
| Bus Stand | 4 km |
| Hospital | 3 km |
| Shopping Mall | 6 km |
| Airport | 8 km |
| University | 10 km |

*Note: These results correspond to the road network defined in this project.*

## How to Run the Project
1. Download or clone this repository.
2. Make sure Python 3 is installed on your computer.
3. Open the project folder.
4. Run the Python file using the following command:

   ```bash
   python main.py
   ```

5. View the output in the terminal.

Alternatively, copy the Python code into an online Python compiler such as Programiz and run it.

## Applications
- City transportation planning
- Road network optimization
- Shortest-route calculation
- Connectivity analysis
- Transportation infrastructure planning
- Network design and optimization

## Conclusion
This project demonstrates how graph data structures and algorithms can be applied to a city transportation network. BFS and DFS help explore network connectivity, Kruskal's algorithm identifies a minimum spanning tree, and Dijkstra's algorithm calculates shortest routes. These techniques provide a basic foundation for understanding transportation network analysis and optimization.

## Author
**Student Project — City Transportation Network**

## License
This project is intended for educational purposes.
