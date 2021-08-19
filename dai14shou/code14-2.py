INF = 1 << 60

N = 6
M = 12
s = 0

# 隣接リスト表記, 重み付き
edges = [
    [[1, 3], [3, 100]],
    [[2, 50], [3, 57], [4, -4]],
    [[3, -10], [4, -5], [5, 100]],
    [[1, -5]],
    [[2, 57], [3, 25], [5, 8]],
    [],
]

exist_negative_cycle = False
dist = [INF]*N
dist[s] = 0

for i in range(N):
    update = False
    for v in range(N):
        if dist[v] == INF:
            continue
        for edge in edges[v]:
            if dist[edge[0]] > dist[v] + edge[1]:
                dist[edge[0]] = dist[v] + edge[1]
                update = True
    if update == False:
        break
    if i == N-1 and update:
        exist_negative_cycle = True

print("Negative cycle: ", exist_negative_cycle)
print(dist)
