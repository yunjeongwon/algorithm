import sys
input = sys.stdin.readline

n = int(input())
t = [0]
p = [0]
dp = [0] * (n + 2)
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

for i in range(1, n + 1):
    for j in range(i + t[i], n + 2):
        if dp[j] < dp[i] + p[i]:
            dp[j] = dp[i] + p[i]

print(dp[n + 1])