import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
g = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            g[r][c] = 1

def f(sr, sc):
    qu = deque()
    qu.append([sr, sc])
    visited[sr][sc] = 1
    res = 1
    while qu:
        cr, cc = qu.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] == 0 and g[nr][nc] == 0:
                visited[nr][nc] = 1
                qu.append([nr, nc])
                res += 1
    return res

visited = [[0] * n for _ in range(m)]
cnt = 0
ans = []
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and g[i][j] == 0:
            res = f(i, j)
            cnt += 1
            ans.append(res)

ans.sort()
print(cnt)
print(*ans)