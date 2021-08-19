#フロイドワーシャル法

INF=1<<60

N,M=6,9
dp=[[INF]*N for _ in range(N)]#N×Nの2次元リスト
#初期化
#dp[a][b]=w
dp[0][1]=3
dp[0][2]=5
dp[1][2]=4
dp[1][3]=12
dp[2][3]=9
dp[2][4]=4
dp[4][3]=7
dp[3][5]=2
dp[4][5]=8

for v in range(N):
    dp[v][v]=0

#更新
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

#負閉路の存在確認
exist_negative_cycle=False
for v in range(N):
    if dp[v][v]<0:
        exist_negative_cycle=True

if exist_negative_cycle:
    print('Negative cycle!')
else:
    for i in range(N):
        for j in range(N):
            if dp[i][j]<INF/2:
                print(dp[i][j], end=' ')
            else:
                print('INF', end=' ')
        print(' ')