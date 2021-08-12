#dfsによる二部グラフ判定
from collections import deque
n=5
graph=[[] for _ in range(n)]
edges=[[0,1],[1,2],[1,4],[3,4],[3,0]]
for i in range(len(edges)):
    a,b=edges[i][0],edges[i][1]
    graph[a].append(b)
    graph[b].append(a)
#色。-1：未探索、0：白、1：黒
color=[-1]*n

def dfs(v,cur=0):#頂点、色
    color[v]=cur

    for nv in graph[v]:
        if color[nv]!=-1:
            if color[nv] == cur:
                return False
            continue
        if not dfs(nv,1-cur):
            return False
    return True

is_bipartite=True

for v in range(n):
    if color[v] != -1:
        continue
    if not dfs(v):
        is_bipartite=False

if is_bipartite:
    print('Yes')
else:
    print('No')