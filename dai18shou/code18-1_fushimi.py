#頂点数
n=int(input())
w=[0]*n
#頂点の重み
for i in range(n):
    w[i]=int(input())
graph=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v,p=-1):
    #子頂点の探索
    for ch in graph[v]:
        if ch == p:#親はskip
            continue
        dfs(ch,v)
    
    #帰りがけの処理
    dp1[v]=0
    dp2[v]=w[v]
    for ch in graph[v]:
        if ch == p:
            continue
        dp1[v] += max(dp1[ch],dp2[ch])
        dp2[v] += dp1[ch]


root=0
dp1=[0]*n
dp2=[0]*n

dfs(root)


print(max(dp1[root],dp2[root]))