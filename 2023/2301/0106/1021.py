import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
qu = deque([i for i in range(1, N + 1)])
arr = list(map(int, input().split()))
ans = 0
for cur in arr:
    while True:
        idx = qu.index(cur)
        if idx == 0:
            qu.popleft()
            break
        else:
            if len(qu) // 2 >= idx:
                qu.append(qu.popleft())
                ans += 1
            else:
                qu.appendleft(qu.pop())
                ans += 1
print(ans)