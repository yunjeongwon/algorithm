import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

qu = deque()
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            qu.append([i, j])
            visited[i][j] = 1
ans = 1
while qu:
    cr, cc = qu.popleft()

    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and G[nr][nc] == 0:
            visited[nr][nc] = visited[cr][cc] + 1
            G[nr][nc] = 1
            qu.append([nr, nc])
            ans = visited[nr][nc]

for i in range(N):
    if G[i].count(0):
        print(-1)
        exit()
print(ans - 1)
