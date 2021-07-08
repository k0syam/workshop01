coinvalue = [500, 100, 50, 10, 5, 1]
a = [1, 5, 3, 6, 2, 5]
X = 876

result = 0
for i in range(6):
    # 枚数制限がない場合
    add = X // coinvalue[i]
    # 枚数制限を考慮
    if add > a[i]:
        add = a[i]
    X -= coinvalue[i] * add
    result += add

print(result)
