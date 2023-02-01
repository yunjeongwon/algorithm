T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 10001)

    for coin in arr:
        dp[coin] += 1
        for i in range(coin, M + 10001):
            dp[i] += dp[i - coin]
    print(dp[M])
