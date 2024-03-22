class Directed:
    def __init__(self):
        self.mat = []

    def add_vertex(self):
        self.mat.append([])
        for node in self.mat:
            while len(node) < len(self.mat):
                node.append(0)

    def add_edge(self, source, dest, weight):
        while source >= len(self.mat) or dest >= len(self.mat):
            self.add_vertex()
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

    def is_valid_path(self, path):
        if len(path) == 0:
            return True
        for step in range(len(path) - 1):
            if path[step] > len(self.mat) or path[step + 1] > len(self.mat):
                return False
            elif self.mat[path[step]][path[step + 1]] == 0:
                return False
        return True


if __name__ == "__main__":
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = Directed()
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))
