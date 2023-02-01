import sys
input = sys.stdin.readline

G = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if G[i][j] == 0:
            blank.append([i, j])

def f(v):
    if v == len(blank):
        for i in G:
            print(*i)
        exit()
        return

    cr, cc = blank[v]
    # 3x3
    tmp = [100] + [0] * 9
    for i in range(cr // 3 * 3, cr // 3 * 3 + 3):
        for j in range(cc // 3 * 3, cc // 3 * 3 + 3):
            if G[i][j] != 0:
                tmp[G[i][j]] = 1
    # 가로
    for i in range(9):
        if G[cr][i] != 0:
            tmp[G[cr][i]] = 1

    for i in range(9):
        if G[i][cc] != 0:
            tmp[G[i][cc]] = 1
    for i in range(1, 10):
        if tmp[i] == 0:
            G[cr][cc] = i
            f(v + 1)
            G[cr][cc] = 0

f(0)
