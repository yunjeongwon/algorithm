import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, n + 1):
    if i == 1:
        for j in range(10):
            dp[i][j] = 1
    else:
        sumV = 0
        for j in range(10):
            sumV += dp[i - 1][j]
            dp[i][j] = sumV
print(sum(dp[n]) % 10007)
