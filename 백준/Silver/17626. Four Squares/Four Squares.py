import math
import sys
input = sys.stdin.readline

n = int(input())

INF = 10 ** 9

dp = [INF] * 50001

for i in range(1, 224):
    dp[i ** 2] = 1

for i in range(2, n + 1):
    rooted = int(math.sqrt(i))
    minV = INF
    for j in range(rooted, 0, -1):
        tmp = 1 + dp[i - j ** 2]
        if minV > tmp:
            minV = tmp
    dp[i] = min(dp[i], minV)


print(dp[n])