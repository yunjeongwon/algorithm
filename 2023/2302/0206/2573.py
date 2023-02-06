import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

def bfs(sr, sc, visited):
    qu = deque()
    qu.append([sr, sc])
    visited[sr][sc] = 1
    while qu:
        cr, cc = qu.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and g[nr][nc] != 0:
                visited[nr][nc] = 1
                qu.append([nr, nc])
    return visited

def over2():
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for cr in range(n):
        for cc in range(m):
            if g[cr][cc] != 0 and visited[cr][cc] == 0:
                visited = bfs(cr, cc, visited)
                cnt += 1
                if cnt >= 2:
                    return True

def is0():
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for cr in range(n):
        for cc in range(m):
            if g[cr][cc] != 0 and visited[cr][cc] == 0:
                visited = bfs(cr, cc, visited)
                cnt += 1
    if cnt == 0:
        return True

ans = 0
while True:
    if over2():
        break
    cand = []
    for cr in range(n):
        for cc in range(m):
            if g[cr][cc] != 0:
                cnt = 0
                for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < m and g[nr][nc] == 0:
                        cnt += 1
                cand.append([cr, cc, cnt])
    if not cand:
        break
    for cr, cc, cnt in cand:
        if g[cr][cc] - cnt < 0:
            g[cr][cc] = 0
        else:
            g[cr][cc] -= cnt
    if is0():
        print(0)
        exit()
    ans += 1
print(ans)
