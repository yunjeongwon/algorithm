import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def f(s):
    qu = deque()
    visited = [-1] * (n + 1)
    qu.append(s)
    visited[s] = 0
    while qu:
        cur = qu.popleft()

        for i in g[cur]:
            if visited[i] == -1:
                visited[i] = visited[cur] + 1
                qu.append(i)
    res = 0
    for i in range(1, len(visited)):
        res += visited[i]
    return res

minV = float('inf')
ans = 0
for i in range(1, n + 1):
    res = f(i)
    if minV > res:
        minV = res
        ans = i
print(ans)