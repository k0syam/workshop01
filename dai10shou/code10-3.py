#グラフを入力として受け取る

#頂点数と辺数
n, m = map(int,input().split())

g=[[] for _ in range(n)]

for i in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    #無向グラフの場合
    #g[b].append(a)

print(g)