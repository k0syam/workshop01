def chmin(a, b):
    if a > b:
        return b
    else:
        return a

S = list("logistic")
T = list("algorithm")
INF = 1000000000000000000000
dp = [[INF for j in range(len(T) + 1)] for i in range(len(S) + 1)]
dp[0][0] = 0
for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        if i > 0 and j > 0:
            # 変更操作
            if S[i-1] == T[j-1]:
                dp[i][j] = chmin(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j] = chmin(dp[i][j], dp[i-1][j-1] + 1)
        # 削除操作
        if i > 0:
            dp[i][j] = chmin(dp[i][j], dp[i-1][j] + 1)
        # 挿入操作
        if j > 0:
            dp[i][j] = chmin(dp[i][j], dp[i][j-1] + 1)

print(dp[-1][-1])