#dfsによる根無し木の走査
from collections import deque
n=5
graph=[[] for _ in range(n)]
edges=[[0,1],[1,2],[1,4],[3,4],[3,0]]
for i in range(len(edges)):
    a,b=edges[i][0],edges[i][1]
    graph[a].append(b)
    graph[b].append(a)

def dfs(v,p=-1):#v:頂点、p:vの親

    for c in graph[v]:
        if c==p:#親への逆流を防ぐ
            continue
        dfs(c,v)
