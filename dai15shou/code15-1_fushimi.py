#Union-Findの実装
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

#辺e=(u,v)を[w(e),u,v]で表す
#n,m=頂点数、辺数
n,m=8,12
edges=[]
edges.append([4,1,4])
edges.append([2,6,4])
edges.append([3,1,6])
edges.append([9,2,4])
edges.append([8,1,3])
edges.append([7,6,7])
edges.append([5,2,7])
edges.append([6,3,7])
edges.append([3,7,0])
edges.append([5,3,0])
edges.append([10,2,5])
edges.append([6,0,5])
#重みが小さい順にソート
edges.sort()


res=0
uf=UnionFind(n)
for i in range(m):
    [w,u,v]=edges[i]
    #w,u,v=edges[i][0],edges[i][1],edges[i][2]

    #u,vが既に同じグループなら辺を追加しない
    if uf.issame(u,v):
        continue
    #辺を追加
    res += w
    uf.unite(u,v)

print(res)
