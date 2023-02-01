import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visited = [0] * (N + 1)
qu = deque()
qu.append(1)
visited[1] = 1
while qu:
    cur = qu.popleft()

    for new in G[cur]:
        if visited[new] == 0:
            visited[new] = 1
            qu.append(new)
ans = 0
for i in visited:
    if i == 1:
        ans += 1
print(ans - 1)