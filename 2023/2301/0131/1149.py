import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(3):
        minV = float('inf')
        for k in range(3):
            if j == k:
                continue
            minV = min(minV, g[i - 1][k])
        g[i][j] += minV

print(min(g[n - 1]))