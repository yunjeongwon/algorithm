import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]

minV = 101
maxV = 0
for i in range(n):
    for j in range(n):
        minV = min(minV, G[i][j])
        maxV = max(maxV, G[i][j])

def bfs(sr, sc):
    qu = deque()
    qu.append([sr, sc])
    after[sr][sc] = 1
    while qu:
        cr, cc = qu.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < n and after[nr][nc] == 0:
                after[nr][nc] = 1
                qu.append([nr, nc])

ans = 0
for rain in range(minV - 1, maxV + 1):
    after = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] <= rain:
                after[i][j] = 1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if after[i][j] == 0:
                cnt += 1
                bfs(i, j)
    ans = max(ans, cnt)
print(ans)