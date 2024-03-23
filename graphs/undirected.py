
class Undirected:
    def __init__(self, edges = None):
        self.adjacency_list = dict()
        if edges != None:
            for e in edges:
                self.add_edge(e[0], e[1])
    
    def add_vertex(self, name: str):
        if name in self.adjacency_list:
            return
        self.adjacency_list[name] = []
        
    def add_edge(self, v1: str, v2: str):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)
    
    def remove_edge(self, v1: str, v2: str):
        if v1 in self.adjacency_list[v2]:
            self.adjacency_list[v1].remove(v2)
            self.adjacency_list[v2].remove(v1)
            
    def remove_vertex(self, name: str):
        if name in self.adjacency_list:
            for v in self.adjacency_list:
                self.remove_edge(name, v)
            del self.adjacency_list[name]
            
    def get_vertices(self):
        vertices = []
        for v in self.adjacency_list:
            vertices.append(v)
        return vertices
    
    def get_edges(self):
        edges = []
        for v in self.adjacency_list:
            for e in self.adjacency_list[v]:
                if (e, v) in edges:
                    continue
                else:
                    edges.append((v, e))
        return edges
    
    def valid_path(self, path: str):
        for index in range(len(path) - 1):
            if path[index] in self.adjacency_list:
                if path[index + 1] in self.adjacency_list[path[index]]:
                    continue
                else:
                    return False
        return True
    
    def dfs(self, v1, v2 = None):
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
           
    def bfs(self, v1, v2 = None):
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
