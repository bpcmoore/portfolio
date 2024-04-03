from undirected import Undirected as Und

if __name__ == "__main__":
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = Und(edges)
    print("\nInitiated Graph", g, "#" * 3 * len(g.get_edges()))
    g.add_vertex('J')
    print("\nAdded Vertex J", g, "#" * 3 * len(g.get_edges()))
    g.add_edge('J', 'Q')
    print("\nAdded Edge from Q to J", g, "#" * 3 * len(g.get_edges()))
    g.remove_edge('Q', 'J')
    print("\nRemoved Edge from Q to J", g, "#" * 3 * len(g.get_edges()))
    g.remove_vertex('J')
    print("\nRemoved Vertex J", g, "#" * 3 * len(g.get_edges()))
    print("\nList of Vertices\n", g.get_vertices(), "\n",
          "#" * 3 * len(g.get_edges()))
    print("\nList of Edges\n", g.get_edges(), "\n",
          "#" * 3 * len(g.get_edges()))
    print("\nTesting Path ECABDCBE: ", g.is_valid_path('ECABDCBE'), "\n",
          "#" * 3 * len(g.get_edges()))
    out = "\nDepth First Search from each Vertex\n"
    for vert in g.get_vertices():
        out += "{}: {}\n".format(vert, g.dfs(vert))
    out += "#" * 3 * len(g.get_vertices()) + \
        "\n\nBreadth First Search from each Vertex\n"
    for vert in g.get_vertices():
        out += "{}: {}\n".format(vert, g.bfs(vert))
    print(out)
