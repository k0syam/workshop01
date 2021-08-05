N = 8
a = [3, 8, 1, 0, 34, 9, 18, 4]

def merge_sort(left, right):
    if right - left == 1:
        return
    mid = left + (right - left) // 2

    merge_sort(left, mid)
    merge_sort(mid, right)

    buf = []
    for i in range(left, mid):
        buf.append(a[i])
    for i in range(right-1, mid, -1):
        buf.append(a[i])
    index_left = 0
    index_right = len(buf)-1
    for i in range(left, right-1):
        if buf[index_left] <= buf[index_right]:
            a[i] = buf[index_left]
            index_left += 1
        else:
            a[i] = buf[index_right]
            index_left -= 1


merge_sort(0, N)
print(a)