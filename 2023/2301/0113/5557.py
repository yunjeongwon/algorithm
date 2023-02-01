import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]
dp[0][arr[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j] != 0:
            for k in [-1, 1]:
                tmp = j + arr[i] * k
                if 0 <= tmp <= 20:
                    dp[i][tmp] += dp[i - 1][j]

print(dp[-2][arr[-1]])
