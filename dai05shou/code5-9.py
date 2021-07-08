def chmin(dp:list,i,x):
  if x<dp[i]:
    dp[i]=x
    return True
  return False

INF= 1<<60

n=int(input())
c=[0]*n
for i in range(n):
    c[i]=list(map(int,input().split()))

dp=[INF]*(n+1)
dp[0]=0

for i in range(n+1):
    for j in range(i):
        chmin(dp,i,dp[j]+c[j][i])

print(dp[n])