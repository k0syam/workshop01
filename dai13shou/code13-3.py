from collections import deque
n=9
graph=[[] for _ in range(n)]
#for i in range(n):
#    a=i
#    b=(i+1)%n
#    graph[a].append(b)
#    graph[b].append(a)
#print(graph)
graph=[[1,4,2],[0,3,4,8],[0,5],[1,7,8],[0,1,8],[2,6,8],[5,7],[3,6],[1,3,4,5]]

dist=[-1]*n
todo=deque()

s=0
dist[s]=0
todo.append(s)

while todo:
    #print(todo)
    v=todo.popleft()

    #vからたどれる頂点を全て調べる
    for x in graph[v]:
        if dist[x]!=-1:
            continue
        dist[x]=dist[v]+1
        #distの小さいところから探索しているので
        #後からより小さい値で上書きされることはない
        todo.append(x)

print(dist)

