import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

qu = deque([i for i in range(1, N + 1)])
arr = []
while True:
    if qu:
        for _ in range(K - 1):
            qu.append(qu.popleft())
        arr.append(qu.popleft())
    else:
        break
print("<", end="")
print(', '.join(map(str, arr)), end="")
print(">")
