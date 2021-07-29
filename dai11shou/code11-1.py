#Union-Find,経路圧縮の工夫無しの場合の根の取得

def root(x):
    if par[x] == -1:
        return x
    else:
        return root(par[x])
