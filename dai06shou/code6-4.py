import bisect
INF = 1<<120
N = 3
K = 8
a = [6, 2, 10]
b = [3, 4, 5]

min_value = INF

b.sort()

for i in range(N):
    iter = bisect.bisect_left(b, K - a[i])
    if iter <= N-1:
        if b[iter] + a[i] < min_value:
            min_value = b[iter] + a[i]

print(min_value)