import heapq

INF = 1 << 60

N = 6
M = 10
s = 0

# 隣接リスト表記, 重み付き
edges = [
    [[1, 3], [3, 100]],
    [[2, 50], [3, 57], [4, 54]],
    [[3, 210], [4, 65], [5, 100]],
    [[1, 555]],
    [[2, 57], [3, 25], [5, 8]],
    [],
]

dist = [INF]*N
dist[s] = 0

que = [[dist[i], i] for i in range(N)]
heapq.heapify(que)

while(que != []):
    d, v = que[0]
    heapq.heappop(que)
    if d > dist[v]:
        continue
    for edge in edges[v]:
        if dist[edge[0]] > dist[v] + edge[1]:
            dist[edge[0]] = dist[v] + edge[1]
            heapq.heappush(que, [dist[edge[0]], edge[0]])

print(dist)

        