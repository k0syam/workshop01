memo = [-1 for i in range(50)]

def fibo(N):
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1
    if memo[N] != -1:
        return memo[N]
    else:
        memo[N] = fibo(N-1) + fibo(N-2)
        return memo[N]

if __name__=="__main__":
    fibo(49)
    for i in range(2, 50):
        print(str(i)+"項目：　"+str(memo[i]))
