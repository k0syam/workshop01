N = 3
A = [4, 6, 7]
B = [2, 3, 5]
total = 0
for i in range(N-1, -1, -1):
    A[i] += total
    amari = A[i] % B[i]
    D = 0
    if amari != 0:
        D = B[i] - amari
    total += D

print(total)
