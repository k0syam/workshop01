INF=1<<60
#頂点数、辺数、始点
N,M,s=6,9,0
#graph=[[[行先、重み]のリスト] for _ in range(辺)]
graph=[[[1,3],[2,5]],[[2,4],[3,12]],[[3,9],[4,4]],[[5,2]],[[5,8]],[]]

print(graph[0])
print(graph[1])
print(graph[2])
print(graph[3])
print(graph[4])
print(graph[5])

#ダイクストラ法
used=[False]*N#使用済かどうか(v∈Sかどうか)
dist=[INF]*N#距離
dist[s]=0

for ite in range(N):
    #使用済みでない頂点のうちdist値が最小の頂点を探す
    dist_min=INF
    v_min=-1
    for v in range(N):
        if not used[v] and dist[v] < dist_min:
            dist_min=dist[v]
            v_min=v
    if v_min==-1:
        break

    #上記で選ばれた頂点v_minから出る辺について緩和を行う
    for [v,w] in graph[v_min]:#[頂点、重み]
        dist[v]=min(dist[v],dist[v_min]+w)
    
    used[v_min]=True

for v in range(N):
    if dist[v] < INF:
        print(dist[v])
    else:
        print('INF')




