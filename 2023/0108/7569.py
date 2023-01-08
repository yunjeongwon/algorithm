import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
G = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
qu = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if G[i][j][k] == 1:
                qu.append([i, j, k])
                visited[i][j][k] = 1

ans = 1
while qu:
    ci, cj, ck = qu.popleft()

    for di, dj, dk in [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1]]:
        ni, nj, nk = ci + di, cj + dj, ck + dk
        if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and visited[ni][nj][nk] == 0 and G[ni][nj][nk] == 0:
            visited[ni][nj][nk] = visited[ci][cj][ck] + 1
            ans = visited[ni][nj][nk]
            qu.append([ni, nj, nk])
            G[ni][nj][nk] = 1

def f():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if G[i][j][k] == 0:
                    return 0
    return 1

if f():
    print(ans - 1)
else:
    print(-1)
