class Graph:
    def __init__(self, N, edges):
        self.N = N
        self.edges = edges
        self.depth = []

    def next_v(self, v):
        buf = []
        for edge in self.edges:
            if edge[0] == v:
                buf.append(edge[1]) 
        return buf

    def dfs(self, v, p=-1, d=0):
        # vを訪問済みにする
        self.depth[v] = d
        if self.next_v(v) != []:
            for next_node in self.next_v(v):
                if next_node == p:
                    continue
                self.dfs(next_node, v, d=d+1)

N, M = 5, 4
edges = [[0, 2],
         [1, 3],
         [2, 3],
         [3, 4]]

graph = Graph(N, edges)
graph.dfs(0)
print(graph.depth)

