N, v = [int(s) for s in input().split()]
a = [int(input()) for i in range(N)]

found_id = -1

for i in range(N):
    if a[i] == v:
        found_id = i
        break

print(found_id)
