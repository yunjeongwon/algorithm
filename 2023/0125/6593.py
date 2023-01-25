import sys
input = sys.stdin.readline
from collections import deque

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    arr3 = []
    for _ in range(l):
        arr2 = [list(input().rstrip()) for _ in range(r)]
        input()
        arr3.append(arr2)

    sf = sr = sc = -1
    ef = er = ec = -1
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr3[i][j][k] == "S":
                    sf, sr, sc = i, j, k
                if arr3[i][j][k] == "E":
                    ef, er, ec = i, j, k

    ans = 0
    qu = deque()
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    qu.append([sf, sr, sc])
    visited[sf][sr][sc] = 1
    while qu:
        cf, cr, cc = qu.popleft()

        if cf == ef and cr == er and cc == ec:
            ans = visited[cf][cr][cc] - 1

        for df, dr, dc in [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1]]:
            nf, nr, nc = cf + df, cr + dr, cc + dc
            if 0 <= nf < l and 0 <= nr < r and 0 <= nc < c and visited[nf][nr][nc] == 0 and arr3[nf][nr][nc] != "#":
                visited[nf][nr][nc] = visited[cf][cr][cc] + 1
                qu.append([nf, nr, nc])
    if ans == 0:
        print("Trapped!")
    else:
        print(f"Escaped in {ans} minute(s).")
