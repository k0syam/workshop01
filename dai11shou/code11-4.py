class UnionFind:
    def __init__(self, n):
        self.par = [-1 for i in range(n)]
        self.siz = [1 for i in range(n)]

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    def is_same(self, x, y):
        return self.root(x) == self.root(y)
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.siz[x] < self.siz[y]:
            y, x = x, y
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True
    
    def size(self, x):
        return self.siz[self.root(x)]

N = 5
M = 3
edges = [[0, 1], [1, 3], [0, 4]]

uf = UnionFind(N)
for a, b in edges:
    uf.unite(a, b)

res = 0
for i in range(N):
    if uf.root(i) == i:
        res += 1

print(res)
