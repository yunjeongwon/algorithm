import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(1, n + 1):
    for j in range(10):
        if 0 <= j - 1:
            dp[i][j] += dp[i - 1][j - 1]
        if j + 1 < 10:
            dp[i][j] += dp[i - 1][j + 1]
print(sum(dp[n]) % 10 ** 9)