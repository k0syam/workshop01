# code11-3から引用
class UnionFind:
    def __init__(self,n):
        self.par=[-1]*n
        self.siz=[1]*n
    
    #根を求める
    def root(self,x):
        if self.par[x] == -1:
            return x
        else:
            #経路圧縮
            self.par[x]=self.root(self.par[x])
            return self.par[x]
    
    #グループ判定(根が一致するかどうか)
    def issame(self,x,y):
        return self.root(x) == self.root(y)
    
    #xとyを併合する
    def unite(self,x,y):
        #根まで移動する
        x=self.root(x)
        y=self.root(y)

        if x==y:
            return False

        #union by size(y側のサイズを小さく)
        if self.siz[x] < self.siz[y]:
            tmp=y
            y=x
            x=tmp
        
        self.par[y]=x
        self.siz[x] += self.siz[y]
        return True
    
    #xを含むグループのサイズ
    def size(self,x):
        return self.siz[self.root(x)]

N = 8
edges = [
    [9, [2, 4]],
    [10, [2, 5]],
    [2, [4, 6]],
    [7, [6, 7]],
    [5, [2, 7]],
    [3, [0, 7]],
    [6, [0, 5]],
    [5, [0, 3]],
    [8, [1, 3]],
    [3, [1, 6]],
    [4, [1, 4]],
    [6, [3, 7]],
]

edges.sort(key = lambda x: x[0])
res = 0
uf = UnionFind(N)

for i in range(len(edges)):
    w = edges[i][0]
    u = edges[i][1][0]
    v = edges[i][1][1]

    if uf.issame(u, v):
        continue

    res += w
    uf.unite(u, v)

print(res)