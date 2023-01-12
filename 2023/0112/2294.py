import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(set([int(input().rstrip()) for _ in range(n)]))

dp = [1e9] * (k + 1)
dp[0] = 0

for num in arr:
    for i in range(k + 1):
        if i - num >= 0:
            dp[i] = min(dp[i], dp[i - num] + 1)
if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])
