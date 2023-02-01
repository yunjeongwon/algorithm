import sys
input = sys.stdin.readline

dp = [[0] * 3 for _ in range(11)]

dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [2, 1, 1]

for i in range(4, 11):
    a = dp[i - 1][0] + dp[i - 2][0] + dp[i - 3][0]
    b = dp[i - 1][1] + dp[i - 2][1] + dp[i - 3][1]
    c = dp[i - 1][2] + dp[i - 2][2] + dp[i - 3][2]
    dp[i] = [a, b, c]

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(dp[n]))
