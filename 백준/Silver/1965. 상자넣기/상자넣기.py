import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = []
dp.append(arr[0])
ans = 0
for i in range(1, n):
    if dp[-1] >= arr[i]:
        idx = 0
        for j in range(len(dp)):
            if dp[j] >= arr[i]:
                idx = j
                break
        dp[idx] = arr[i]
    else:
        dp.append(arr[i])
    ans = max(ans, len(dp))
# print(dp)
print(ans)