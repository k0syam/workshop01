N = 6
w = [3, 2, 1, 6, 10, 6]
G = [[1],
     [0, 2, 3],
     [1, 4, 5],
     [1],
     [2],
     [2]]
dp1 = [0 for i in range(N)]
dp2 = [w[i] for i in range(N)]

def dfs(v, p=-1):
    for ch in G[v]:
        if ch == p:
            continue
        dfs(ch, v)
    dp1[v] = 0
    dp2[v] = w[v]
    for ch in G[v]:
        if ch == p:
            continue
        dp1[v] += max(dp1[ch], dp2[ch])
        dp2[v] += dp1[ch]

root = 0
dfs(root)
print(max(dp1[root], dp2[root])) 
