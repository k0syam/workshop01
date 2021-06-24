def GCD(m, n):
    if n == 0:
        return m
    else:
        return GCD(n, m%n)

if __name__ == "__main__":
    print(GCD(51, 15))
    print(GCD(15, 51))
