par = [-1, 0, 1, 2, 3, 3, 5]

def root(x):
    if par[x] == -1:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

print(par)
root(6)
print(par)