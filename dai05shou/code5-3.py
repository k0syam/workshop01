#Frog問題を緩和を意識したDPで解く

#pythonにchminが無いのでつくる
#リスト自体を引数に渡す(参照)
def chmin(dp:list,i,x):
  if x<dp[i]:
    dp[i]=x
    return True
  return False

INF=1<<60
#2^60
n=int(input())
h=list(map(int,input().split()))

#dp[i]=i番目の地点へ到達する最小コスト
dp=[INF]*n
dp[0]=0
dp[1]=abs(h[1]-h[0])

for i in range(2,n):
    chmin(dp,i,dp[i-1]+abs(h[i]-h[i-1]))
    chmin(dp,i,dp[i-2]+abs(h[i]-h[i-2]))


print(dp[n-1])
