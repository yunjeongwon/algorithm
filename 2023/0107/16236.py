import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
size = 2
eat = 0
ans = 0
def f():
    global size, eat, ans
    qu = deque()
    visited = [[0] * N for _ in range(N)]
    flag = 0
    pos = []
    for i in range(N):
        for k in range(N):
            if G[i][k] == 9:
                pos = [i, k]
                flag = 1
                break
        if flag:
            break
    qu.append(pos)
    visited[pos[0]][pos[1]] = 1
    tmp = []
    while qu:
        cr, cc = qu.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if G[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] + 1
                    qu.append([nr, nc])
                elif G[nr][nc] <= size:
                    visited[nr][nc] = visited[cr][cc] + 1
                    if G[nr][nc] == size:
                        qu.append([nr, nc])
                    else:
                        tmp.append([nr, nc, visited[nr][nc] - 1])
    if tmp:
        tmp.sort(key=lambda x: (x[2], x[0], x[1]))
        ans += visited[tmp[0][0]][tmp[0][1]] - 1
        G[tmp[0][0]][tmp[0][1]] = 9
        G[pos[0]][pos[1]] = 0
        eat += 1
        if eat == size:
            eat = 0
            size += 1
        return True
while f():
    pass
print(ans)
