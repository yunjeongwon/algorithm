import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        for ii in range(i - 1, -1, -1):
            diff = i - ii
            if diff == g[ii][j]:
                dp[i][j] += dp[ii][j]
        for jj in range(j - 1, -1, -1):
            diff = j - jj
            if diff == g[i][jj]:
                dp[i][j] += dp[i][jj]
print(dp[n - 1][n - 1])
