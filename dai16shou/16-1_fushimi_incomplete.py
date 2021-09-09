class Edge:
    def __init__(self,r,f,t,c):
        self.rev=r
        self.fr=f
        self.to=t
        self.cap=c

class Graph:
    def __init__(self,n):
        self.li=[[] for _ in range(n)]
    
    #頂点数取得
    def size(self):
        return len(self.li)
    
    #逆辺取得
    def redge(self,e):
        return self.li[e.to][e.rev]
    
    #フローを流す
    def run_flow(self,e,f):
        e.cap -= f
        self.redge(e).cap += f
    
    #頂点frから頂点toへ容量capの辺を張る
    #逆辺も容量0で張っておく
    def addedge(self,fr,to,cap):
        self.fromrev=int(len(self.li[fr]))
        self.torev=int(len(self.li[to]))
        self.li[fr].append(Edge(self.torev,fr,to,cap))
        self.li[to].append(Edge(self.fromrev,to,fr,0))

class FordFulkerson:
    def __init__(self):
        self.INF=1<<30
        self.seen=[]
    
    #dfsでs-tパスを見つける
    #帰り値はパスの最小値

    def fodfs(self,G,v,t,f):
        if v == t:
            return f
        
        self.seen[v]=True
        for e in G.li[v]:
            if self.seen[e.to]:
                continue
            if e.cap==0:
                continue

            #探す
            self.flow=self.fodfs(G,e.to,t,min(f,e.cap))

            if self.flow==0:
                continue
            
            #辺と逆辺の更新
            G.run_flow(e,self.flow)

            return self.flow
        
        return 0
    
    #s-t間の最大流量を求める
    #リターン時のGは残余グラフになる
    def solve(self,G,s,t):
        res=0

        while True:
            self.seen=[False]*len(G.li)
            self.flow=self.fodfs(G,s,t,self.INF)

            if self.flow==0:
                return res
            res += self.flow
        
        return 0

if __name__ == '__main__':
    n,m=map(int,input().split())
    G=Graph(n)
    for i in range(m):
        u,v,c=map(int,input().split())

        G.addedge(u,v,c)
    
    ff=FordFulkerson()
    s,t=0,n-1

    print(ff.solve(G,s,t))



