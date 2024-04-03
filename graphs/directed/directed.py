# Author: Brook Moore
# Last Update: 3/29/2024

class Directed:
    '''Directed class initiates graph matrix and provides methods for altering
    the graph and getting information about the graph'''
    def __init__(self, edges=None):
        '''To include edges when initializing, format edges as a list of
        tuples containing the starting vertex, the destination vertex and the
        weight'''
        self.mat = []

        if edges is not None:
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
        '''creates an additional vertex in the matrix'''
        self.mat.append([])
        for node in self.mat:
            while len(node) < len(self.mat):
                node.append(0)

    def add_edge(self, source, dest, weight):
        '''Method takes the source vertex, the destination vertex and weight
        as parametes. If the source or destination is not in the matrix,
        vertices will be added until the given vertex is in the matrix.'''
        while source >= len(self.mat) or dest >= len(self.mat):
            self.add_vertex()
        self.mat[source][dest] = weight

    def remove_edge(self, source, dest):
        '''Takes the source vertex and destination vertex as parameters. If
        either vertex is not in the matrix, method does nothing.'''
        if source < len(self.mat) and dest < len(self.mat):
            self.mat[source][dest] = 0

    def get_vertices(self):
        '''Returns a list of vertices present in the matrix.'''
        v = []
        for vertices in range(len(self.mat)):
            v.append(vertices)
        return v

    def get_edges(self):
        '''Returns a list of tuples containing the starting vertex, the
        destination vertex and the weight of all edges in the matrix.'''
        edges = []
        for v in range(len(self.mat)):
            for e in range(len(self.mat[v])):
                if self.mat[v][e] != 0:
                    edges.append((v, e, self.mat[v][e]))
        return edges

    def is_valid_path(self, path):
        '''Takes a list of vertices as a parameter and checks if a traversal
        can be along the graph in the order of given vertices.'''
        if len(path) == 0:
            return True
        for step in range(len(path) - 1):
            if path[step] > len(self.mat) or path[step + 1] > len(self.mat):
                return False
            elif self.mat[path[step]][path[step + 1]] == 0:
                return False
        return True

    def dfs(self, start):
        '''Takes a vertex as a parameter and performs a depth first search
        starting at the given vertex.'''
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
        '''Takes a vertex as a parameter and performs a breadth first search
        starting at the given vertex.'''
        bfs = [start]
        queue = [start]
        while len(queue) > 0:
            cur = queue.pop()
            for edge in range(len(self.mat[cur])):
                if edge not in bfs and self.mat[cur][edge] > 0:
                    queue = [edge] + queue
                    bfs.append(edge)
        return bfs

    def dijkstra(self, start):
        '''Takes a vertex as a parameter and returns a list of optimal
        distances to each vertex where the index corresponds to the vertex.'''
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
                elif self.mat[cur][e] != 0 and \
                        self.mat[cur][e] + d[cur] < d[e]:
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
