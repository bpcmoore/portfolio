class Directed:
    def __init__(self):
        self.mat = []

    def add_vertex(self):
        self.mat.append([])
        for node in self.mat:
            while len(node) < len(self.mat):
                node.append(0)

    def add_edge(self, source, dest, weight):
        if source < len(self.mat) and dest < len(self.mat):
            self.mat[source][dest] = weight

    def remove_edge(self, source, dest):
        if source < len(self.mat) or dest < len(self.mat):
            self.mat[source][dest] = 0   

    def get_vertices(self):
        v = []
        for vertices in range(len(self.mat)):
            v.append(vertices)
        return v

    def get_edges(self):
        edges = []
        for v in range(len(self.mat)):
            for e in range(len(self.mat[v])):
                if self.mat[v][e] != 0:
                    edges.append((v, e, self.mat[v][e]))
        return edges


if __name__ == "__main__":
    graph = Directed()
    for i in range(5):
        graph.add_vertex()
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
        (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        graph.add_edge(src, dst, weight)
    graph.remove_edge(0, 1)
    print(graph.mat)
    print(graph.get_edges())
