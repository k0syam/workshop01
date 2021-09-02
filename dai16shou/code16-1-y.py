INF = 1 << 30

class Edge:
    def __init__(self, r, f, t, c):
        self.rev = r
        self.nfrom = f
        self.nto = t
        self.cap = c 

class Graph:
    def __init__(self, N, edges):
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
    def __init__(self, ):
        self.seen = []
    def fodfs(self, Graph, v, t, f):
        if v == t:
            return f
        self.seen[v] = True
        for edgelist in Graph.neilist:
            for e in edgelist:
                if seen[e.to]:
                    continue
                if e.cap == 0:
                    continue
                flow = self.fodfs(Graph, e.to, t, min(f, e.cap))
                if flow == 0:
                    continue
                Graph.run_flow(e, flow)
                return flow
        return 0
    def solve(self, Graph, s, t):
        pass

