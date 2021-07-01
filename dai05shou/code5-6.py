def chmin(a, b):
    if a > b:
        return b
    else:
        return a

N = 10
h = [2, 5, 4, 1, 3, 8, 2, 3, 4, 9]
INF = 1000000000000000000000

dp = [INF for i in range(N)]
dp[0] = 0

def rec(i):
    if dp[i] < INF:
        return dp[i]
    if i == 0:
        return 0
    res = INF
    res = chmin(res, rec(i-1) + abs(h[i] - h[i-1]))
    if i > 1:
        res = chmin(res, rec(i-2) + abs(h[i] - h[i-2]))
    dp[i] = res
    return res

rec(N-1)
print(N-1)