#二分探索
N=8
a=[3,5,8,10,14,17,21,39]

#昇順になっているとは限らないときはa.sort()

def binary_search(key):
    left=0
    right=len(a)-1
    while left <= right:
        mid=left + (right - left)//2
        #pythonでは mid=(right+left)//2 で問題ないハズ
        #C++だと型のサイズの関係でエラーとなる可能性があるらしい
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid - 1
        elif a[mid] < key:
            left = mid + 1
    return -1#キーの値が存在しない

print(binary_search(10))
print(binary_search(3))
print(binary_search(39))
print(binary_search(-100))
print(binary_search(9))
print(binary_search(100))