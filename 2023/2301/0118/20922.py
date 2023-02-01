import sys
input = sys.stdin.readline

cnt = [0] * 100001

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
l = 0
r = 0
cnt[arr[l]] += 1

while l <= r and r < n:
    if cnt[arr[r]] > k:
        cnt[arr[l]] -= 1
        l += 1
        dist = r - l + 1
        ans = max(ans, dist)
    else:
        r += 1
        if r >= n:
            break
        cnt[arr[r]] += 1
        if cnt[arr[r]] > k:
            cnt[arr[l]] -= 1
            l += 1
            continue
        dist = r - l + 1
        ans = max(ans, dist)

print(ans)