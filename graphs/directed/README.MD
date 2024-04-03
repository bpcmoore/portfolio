# directed.py

The Directed class initiates a matrix representation of a graph. Directed can be initialized with or without edges. To initialize a graph with edges, give it a list of tuple with the start vertex, the destination vertex, and the weight of the edge. Edges are unidirectional so to make graph bidirectional you must add the edge twice with each vertex as the start vertex. The Directed class also contains methods to alter the graph and get information from the graph. A list of those methods are shown below.

## Methods
- add_vertex
- add_edge
- remove_edge
- get_vetices
- get_edges
- is_valid_path
- dfs
- bfs
- dijkstra