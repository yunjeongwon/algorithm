import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

qu = deque()
visited = [0] * (n + 1)
qu.append(1)
visited[1] = 1
while qu:
    cur = qu.popleft()

    for new in G[cur]:
        if visited[new] == 0:
            visited[new] = visited[cur] + 1
            qu.append(new)
ans = 0
for i in range(2, n + 1):
    if 0 < visited[i] <= 3:
        ans += 1
print(ans)