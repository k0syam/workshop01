N, W = [int(s) for s in input().split()]
a = [int(input) for i in range(N)]

exist = False

for bit in range(int(bin(1) << bin(N))):
    sum_num = 0
    for i in range(N):
        if bin(bit) & (bin(1) << bin(i))):
            sum_num += a[i]
        if sum_num == W:
            exist = True

if exist:
    print("Yes")
else:
    print("No")
