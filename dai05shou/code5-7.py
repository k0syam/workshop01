#ナップサック問題


#2次元リストのchmax
def chmax(dp:list,i,j,x):
  if x>dp[i][j]:
    dp[i][j]=x
    return True
  return False

N,W=map(int,input().split())
weight=[0]*N
value=[0]*W
for i in range(N):
    weight[i], value[i] = map(int,input().split())

dp=[[0]*(W+1) for _ in range(N+1)]

for i in range(N):#0~N-1まで(0-index)
    for w in range(W+1):#重さ0~Wまで計算必要
        #i番目の荷物を選ぶ場合
        if w - weight[i] >= 0:
            chmax(dp,i+1,w,dp[i][w-weight[i]]+value[i])
        
        #i番目の荷物を選ばない場合
        chmax(dp,i+1,w,dp[i][w])

print(dp[N][W])

print(dp)        