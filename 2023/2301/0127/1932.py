import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    arr = list(map(int, input().split()))
    dp.append(arr)

for i in range(1, n):
    for j in range(i + 1):
        a, b = 0, 0
        if 0 <= j - 1 < n:
            a = dp[i - 1][j - 1]
        if j < i:
            b = dp[i - 1][j]
        dp[i][j] += max(a, b)
print(max(dp[n - 1]))