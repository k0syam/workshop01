#dfsによる根無し木の走査
from collections import deque
n=5
graph=[[] for _ in range(n)]
edges=[[0,1],[1,2],[1,4],[3,4]]
for i in range(len(edges)):
    a,b=edges[i][0],edges[i][1]
    graph[a].append(b)
    graph[b].append(a)

depth=[0]*n
subtree_size=[0]*n

def dfs(v,p=-1,d=0):#v:頂点、p:vの親,d:vの深さ
    depth[v]=d
    subtree_size[v]=1

    for c in graph[v]:
        if c==p:#親への逆流を防ぐ
            continue

        dfs(c,v,d+1)#深さ+1
        #帰りがけ時に部分木サイズの情報を更新
        subtree_size[v] += subtree_size[c]

root=0
dfs(root)

for v in range(n):
    print(v,depth[v],subtree_size[v])





