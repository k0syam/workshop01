def chmin(a, b):
    if a > b:
        return b
    else:
        return a

N = 10
h = [2, 5, 4, 1, 3, 8, 2, 3, 4, 9]

dp = [float("inf") for i in range(N)]
dp[0] = 0
for i in range(N):
    if i + 1 < N:
        dp[i+1] = chmin(dp[i+1], dp[i]+abs(h[i]-h[i+1]))
    if i + 2 < N:
        dp[i+2] = chmin(dp[i+2], dp[i]+abs(h[i]-h[i+2]))

print(dp[N-1])
