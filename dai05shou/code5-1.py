#Frog問題をDPで解く

INF=1<<60
#2^60
n=int(input())
h=list(map(int,input().split()))

#dp[i]=i番目の地点へ到達する最小コスト
dp=[INF]*n
dp[0]=0
dp[1]=abs(h[1]-h[0])

for i in range(2,n):
    a1=dp[i-1]+abs(h[i]-h[i-1])
    a2=dp[i-2]+abs(h[i]-h[i-2])
    dp[i]=min(a1,a2)

print(dp[n-1])
