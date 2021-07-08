#2次元リストのソート
a = [('A', 2), ('B', 3), ('C', 1)]

# 昇順ソート
a.sort(key=lambda x: x[1])
print(a)  #=> [('C', 1), ('A', 2), ('B', 3)]

# 降順ソート
a.sort(key=lambda x: x[1], reverse=True)
print(a)  #=> [('B', 3), ('A', 2), ('C', 1)]