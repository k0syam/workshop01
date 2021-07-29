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
        return siz[self.root(x)]


if __name__ == '__main__':
    uf=UnionFind(7)

    uf.unite(1,2)
    uf.unite(2,3)
    uf.unite(5,6)

    print(uf.issame(1,3))
    print(uf.issame(2,5))

    uf.unite(1,6)

    print(uf.issame(2,5))