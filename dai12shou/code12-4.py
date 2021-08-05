import heapq

# 実装①: そのままheappopすると最小値をpopし続ける
N = 8
a = [3, 8, 1, 0, 34, 9, 18, 4]
heapq.heapify(a)
for _ in range(N):
    print(heapq.heappop(a))


# 実装②: Pythonドキュメンテーションに紹介されている方法
N = 8
a = [3, 8, 1, 0, 34, 9, 18, 4]
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort(a))