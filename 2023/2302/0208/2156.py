import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input().rstrip()) for _ in range(n)]

dp = [[0] * 4 for _ in range(n + 1)]

dp[0] = [arr[0], 0, arr[0], 0]
if n >= 2:
    dp[1] = [arr[0] + arr[1], arr[0], arr[1], 0]

for i in range(2, n):
    dp[i][0] = max(dp[i][0], dp[i - 1][2] + arr[i])
    dp[i][1] = max(dp[i][1], dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = max(dp[i][2], dp[i - 1][1] + arr[i], dp[i - 1][3] + arr[i])
    dp[i][3] = max(dp[i][3], dp[i - 1][1], dp[i - 1][3])

print(max(dp[n - 1]))