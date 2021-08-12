class Graph:
    def __init__(self, N, edges):
        self.seen = [False]*N
        self.edges = edges
        self.order = []

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
        self.order.append(v)

    def make_all_seen_by_dfs(self):
        for i, seen in enumerate(self.seen):
            if seen:
                continue
            self.dfs(i)

N, M = 8, 12
edges = [[4, 2],
         [4, 6],
         [4, 1],
         [1, 6],
         [1, 3],
         [6, 7],
         [2, 7],
         [2, 5],
         [3, 7],
         [7, 0],
         [3, 0],
         [0, 5]]

graph = Graph(N, edges)
graph.make_all_seen_by_dfs()
graph.order.reverse()
print(graph.order)