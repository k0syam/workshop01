from collections import deque
n=10
graph=[[] for _ in range(n)]
for i in range(n):
    a=i
    b=(i+1)%n
    graph[a].append(b)
    graph[b].append(a)
print(graph)

seen=[False]*n
todo=deque()

s=0
seen[s]=True
todo.append(s)

while todo:
    print(todo)
    v=todo.popleft()

    #vからたどれる頂点を全て調べる
    for x in graph[v]:
        if seen[x]:
            continue
        seen[x]=True
        todo.append(x)

