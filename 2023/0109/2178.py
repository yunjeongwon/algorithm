import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
G = [list(map(int, input().rstrip())) for _ in range(N)]

qu = deque()
visited = [[0] * M for _ in range(N)]
qu.append([0, 0])
visited[0][0] = 1
ans = 0
while qu:
    cr, cc = qu.popleft()

    if cr == N - 1 and cc == M - 1:
        ans = visited[cr][cc]
        break

    for dr ,dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and G[nr][nc] == 1:
            visited[nr][nc] = visited[cr][cc] + 1
            qu.append([nr, nc])

print(ans)