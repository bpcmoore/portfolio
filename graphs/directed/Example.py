from directed import Directed as Dir


if __name__ == "__main__":
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5),
             (2, 1, 23), (3, 2, 7)]
    graph = Dir(edges)
    print("Initiated Graph as Matrix\n", graph, "\n",
          "#" * (len(graph.get_vertices()) + 1) * 8, "\n")
    graph.add_vertex()
    print("New Vertex Added\n", graph, "\n",
          "#" * (len(graph.get_vertices()) + 1) * 8, "\n")
    graph.add_edge(1, 5, 20)
    print("Edge Added from One to Five with a Weight of 20\n", graph, "\n",
          "#" * (len(graph.get_vertices()) + 1) * 8, "\n")
    graph.remove_edge(1, 5)
    print("Edge Removed from One to Five\n", graph, "\n",
          "#" * (len(graph.get_vertices()) + 1) * 8, "\n")
    print("Checking Possible Path 0, 1, 4, 3\n",
          graph.is_valid_path([0, 1, 4, 3]), "\n", "#" * 56, "\n")
    print("Checking Possible Path 0, 1, 4, 3\n",
          graph.is_valid_path([0, 3, 2, 1]), "\n", "#" * 56, "\n")
    print("Depth First Search and Breadth First Search on all Nodes\n")
    for start in range(5):
        print(f'{start} DFS:{graph.dfs(start)} BFS:{graph.bfs(start)}')
    print("\n", "#" * 56, "\n")
    print("Finding Minimum Distance from each Node to All the Others\n")
    for start in range(5):
        print(f'{start} Dijkstra:{graph.dijkstra(start)}')
    print("\n", "#" * 56, "\n")
