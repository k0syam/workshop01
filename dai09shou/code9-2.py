from collections import deque
import random

que = deque([random.randint(0, 100) for i in range(20)])

# implement que structures
def is_empty(que):
    return len(que) == 0

def is_full(que, N=100):
    return len(que) >= N

# enque
x = 200
que.append(x)
print(que[-1])

# deque
y = que.popleft()
print(y)