N, K = [int(s) for s in input().split()]
a = [int(input()) for i in range(N)]
b = [int(input()) for i in range(N)]

min_value = 2000000000

for i in range(N):
    for j in range(N):
        if a[i] + b[j] < K:
            continue
        min_value = min(a[i] + b[j], min_value)

print(min_value)
