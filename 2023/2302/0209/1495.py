import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = -1

dp = [[] for _ in range(n + 1)]
dp[0] = [s]

for i in range(1, n + 1):
    now = arr[i - 1]
    if not dp[i - 1]:
        break
    for j in range(len(dp[i - 1])):
        back = dp[i - 1][j]
        if back - now >= 0:
            dp[i].append(back - now)
        if back + now <= m:
            dp[i].append(back + now)
    dp[i] = list(set(dp[i]))
if dp[n]:
    ans = max(dp[n])
print(ans)