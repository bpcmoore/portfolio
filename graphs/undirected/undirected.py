# Author: Brook Moore
# Last Update: 04/01/2024

class Undirected:
    '''Undirected class initiates graph as an adjacency list and provides
    methods for altering the graph and getting information about the graph'''
    def __init__(self, edges=None):
        self.adjacency_list = dict()
        if edges is not None:
            for e in edges:
                self.add_edge(e[0], e[1])

    def add_vertex(self, name: str):
        '''Adds a new vertex of given name to adjacency list.'''
        if name in self.adjacency_list:
            return
        self.adjacency_list[name] = []

    def add_edge(self, v1: str, v2: str):
        '''Adds an edge between two vertices of given name. If either given
        vertex is in the adjacency list, method automatically adds it.'''
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)

    def remove_edge(self, v1: str, v2: str):
        '''Removes an edge between two given vertices.'''
        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            if v1 in self.adjacency_list[v2]:
                self.adjacency_list[v1].remove(v2)
                self.adjacency_list[v2].remove(v1)

    def remove_vertex(self, name: str):
        '''Removes given vertex and all edges associated with vertex.'''
        if name in self.adjacency_list:
            for v in self.adjacency_list:
                self.remove_edge(name, v)
            del self.adjacency_list[name]

    def get_vertices(self):
        '''Returns a list of all vertices in the adjacency list.'''
        vertices = []
        for v in self.adjacency_list:
            vertices.append(v)
        return vertices

    def get_edges(self):
        '''Returns a list of all edges in the adjacency list.'''
        edges = []
        for v in self.adjacency_list:
            for e in self.adjacency_list[v]:
                if (e, v) in edges:
                    continue
                else:
                    edges.append((v, e))
        return edges

    def valid_path(self, path: str):
        '''Takes a string consisting of vertices as a parameter. Returns True
        if the string of vertices is a valid path.'''
        for index in range(len(path) - 1):
            if path[index] in self.adjacency_list:
                if path[index + 1] in self.adjacency_list[path[index]]:
                    continue
                else:
                    return False
        return True

    def dfs(self, v1, v2=None):
        '''Does a depth first search on graph. Requires the starting vertex as
        a parameter but can also take the destination vertex.'''
        stack = [v1]
        dfs = [v1]
        while len(stack) > 0:
            if dfs[-1] == v2:
                break
            cur = stack.pop()
            for e in self.adjacency_list[cur]:
                if e not in dfs:
                    stack.append(cur)
                    stack.append(e)
                    dfs.append(e)
                    break
        return dfs

    def bfs(self, v1, v2=None):
        '''Does a breadth first search on graph. Requires the starting vertex
        as a parameter but can also take the destination vertex.'''
        stack = [v1]
        bfs = [v1]
        while len(stack) > 0:
            if bfs[-1] == v2:
                break
            cur = stack.pop()
            for e in self.adjacency_list[cur]:
                if e not in bfs:
                    stack = [e] + stack
                    bfs.append(e)
        return bfs


if __name__ == "__main__":
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = Undirected(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
        print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')
    g = Undirected(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.valid_path(list(path)))
