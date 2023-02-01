import sys
input = sys.stdin.readline

C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [1e9] * (C + 101)
dp[0] = 0
for cost, num in arr:
    for i in range(num, C + 100):
        dp[i] = min(dp[i], dp[i - num] + cost)
print(min(dp[C:]))
