class Graph:
    def __init__(self, N, edges):
        self.seen = [False]*N
        self.edges = edges

    def next_v(self, v):
        buf = []
        for edge in self.edges:
            if edge[0] == v:
                buf.append(edge[1]) 
        return buf

    def dfs(self, v):
        # vを訪問済みにする
        self.seen[v] = True
        for next_node in self.next_v(v):
            if self.seen[next_node]:
                continue
            self.dfs(next_node)

N, M, s, t = 6, 4, 0, 4
edges = [[0, 1],
         [2, 4],
         [2, 5],
         [5, 1]]

graph = Graph(N, edges)
graph.dfs(s)
if (graph.seen[t]):
    print("Yes")
else:
    print("No")
