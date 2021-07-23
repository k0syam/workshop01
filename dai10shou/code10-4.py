class Edge:
    def __init__(self, to, w):
        self.to = to
        self.w = w
    def print_values(self):
        print(self.to, self.w)

N = 5
M = 6
a = [0, 0, 1, 2, 2, 3]
b = [1, 2, 3, 3, 4, 4]
w = [2, 4, 0, 3, 10, 5]

G = [ [] for i in range(N)]
for i in range(M):
    G[a[i]].append(Edge(b[i], w[i]))

for _ in G:
    [i.print_values() for i in _]