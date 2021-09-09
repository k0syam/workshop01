INF = 1 << 30

class Edge:
    def __init__(self, r, f, t, c):
        self.rev = r
        self.nfrom = f
        self.nto = t
        self.cap = c 

class Graph:
    def __init__(self, N):
        self.N = N
        self.neilist = [[] for i in range(N)]
    def redge(self, edge):
        return self.neilist[edge.nto][edge.rev]
    def addedge(self, nfrom, nto, cap):
        nfromrev = len(self.neilist[nfrom])
        ntorev = len(self.neilist[nto])
        self.neilist[nfrom].append(Edge(ntorev, nfrom, nto, cap))
        self.neilist[nto].append(Edge(nfromrev, nto, nfrom, 0))
    def run_flow(self, edge, f):
        edge.cap -= f
        self.redge(edge).cap += f

class FordFulkerson:
    def __init__(self):
        self.INF = 1 << 30
        self.seen = []
    def fodfs(self, Graph, v, t, f):
        if v == t:
            return f
        self.seen[v] = True
        for e in Graph.neilist[v]:
            if self.seen[e.nto]:
                continue
            if e.cap == 0:
                continue
            flow = self.fodfs(Graph, e.nto, t, min(f, e.cap))
            if flow == 0:
                continue
            Graph.run_flow(e, flow)
            return flow
        return 0
    def solve(self, Graph, s, t):
        res = 0
        while True:
            print("DFS start")
            self.seen = [False for _ in range(Graph.N)]
            flow = self.fodfs(Graph, s, t, self.INF)
            if flow == 0:
                return res
            res += flow
            for graph_edges in Graph.neilist:
                for graph_edge in graph_edges:
                    print(graph_edge.nfrom, graph_edge.nto, graph_edge.cap)
        return 0

N = 6
M = 9
edges = [
    [0, 1, 5],
    [0, 3, 5],
    [1, 2, 4],
    [1, 3, 37],
    [2, 4, 56],
    [2, 5, 9],
    [3, 2, 3],
    [3, 4, 9],
    [4, 5, 2]
]

graph = Graph(N)
for edge in edges:
    graph.addedge(edge[0], edge[1], edge[2])
# print(graph.neilist)
ff = FordFulkerson()
s = 0
t = N-1
print(ff.solve(graph, s, t))