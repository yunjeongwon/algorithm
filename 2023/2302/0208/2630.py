import sys
input = sys.stdin.readline


n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
ansW = 0
ansB = 0
def dfs(sr, sc, size):
    global ansW, ansB
    cntW = 0
    cntB = 0
    for i in range(sr, sr + size):
        for j in range(sc, sc + size):
            if g[i][j] == 0:
                cntW += 1
            else:
                cntB += 1
    if cntW == size ** 2:
        ansW += 1
        return
    if cntB == size ** 2:
        ansB += 1
        return
    dfs(sr, sc, size // 2)
    dfs(sr + size // 2, sc, size // 2)
    dfs(sr, sc + size // 2, size // 2)
    dfs(sr + size // 2, sc + size // 2, size // 2)

dfs(0, 0, n)

print(ansW)
print(ansB)