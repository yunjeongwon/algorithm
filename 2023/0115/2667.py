import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
G = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(sr, sc, res):
    qu = deque()
    qu.append([sr, sc])
    visited[sr][sc] = res
    cnt = 1
    while qu:
        cr, cc = qu.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and G[nr][nc] == 1:
                visited[nr][nc] = res
                qu.append([nr, nc])
                cnt += 1
    return cnt

visited = [[0] * n for _ in range(n)]
res = 0
cntArr = []
for i in range(n):
    for j in range(n):
        if G[i][j] == 1 and visited[i][j] == 0:
            res += 1
            cnt = bfs(i, j, res)
            cntArr.append(cnt)

print(res)
cntArr.sort()
for i in cntArr:
    print(i)