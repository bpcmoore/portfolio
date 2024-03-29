class Directed:
    def __init__(self, edges = None):
        self.mat = []

        if edges != None:
            for edge in edges:
                self.add_edge(edge[0], edge[1], edge[2])

    def __str__(self):
        out = "\t||0\t"
        for i in range(1, len(self.mat)):
            out += "|{}\t".format(i)
        
        for v in range(len(self.mat)):
            out += "\n"
            out += "=" * (len(self.mat) + 1) * 8
            out = out + "\n{}\t||".format(v)
            for e in range(len(self.mat[v])):
                out += "{}\t|".format(self.mat[v][e])
        out += "\n"
        return out

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

    def dfs(self, start):
        dfs = [start]
        stack = [start]
        while len(stack) > 0:
            cur = stack.pop()
            for edge in range(len(self.mat[cur])):
                if edge not in dfs and self.mat[cur][edge] > 0:
                    stack.append(cur)
                    stack.append(edge)
                    dfs.append(edge)
                    break
        return dfs

    def bfs(self, start):
        bfs = [start]
        stack = [start]
        while len(stack) > 0:
            cur = stack.pop()
            for edge in range (len(self.mat[cur])):
                if edge not in bfs and self.mat[cur][edge] > 0:
                    stack = [edge] + stack
                    bfs.append(edge)
        return bfs

    def dijkstra(self, start):
        d = ["infinity"] * len(self.mat)
        d[start] = 0
        queue = [start]
        while len(queue) > 0:
            cur = queue.pop()
            for e in range(len(self.mat[cur])):
                if d[e] == "infinity":
                    if self.mat[cur][e] != 0:
                        d[e] = self.mat[cur][e] + d[cur]
                        queue.append(e)
                elif self.mat[cur][e] != 0 and self.mat[cur][e] + d[cur] < d[e]:
                    d[e] = self.mat[cur][e] + d[cur]
                    queue.append(e)
        return d

if __name__ == "__main__":
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = Directed(edges)

    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    print('\n', g)
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
