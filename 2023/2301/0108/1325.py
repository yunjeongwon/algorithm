import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    # G[a].append(b)
    G[b].append(a)

def f(s):
    qu = deque()
    qu.append(s)
    visited[s] = 1
    cnt = 0
    while qu:
        cur = qu.popleft()

        for new in G[cur]:
            if visited[new] == 0:
                visited[new] = 1
                qu.append(new)
                cnt += 1
    return cnt
res = [0]
maxV = 0
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    cnt = f(i)
    res.append(cnt)
    if maxV < cnt:
        maxV = cnt
for i in range(1, N + 1):
    if res[i] == maxV:
        print(i, end=" ")
print()
