import sys
input = sys.stdin.readline

k = int(input())

arr = [0] * 30
for i in range(1, 30):
    arr[i] = arr[i - 1] + 2 ** i

idx = -1
for i in range(1, 30):
    if arr[i] >= k:
        idx = i
        break
# print(idx, k - arr[idx - 1], 2 ** idx)
order = k - arr[idx - 1]

ans = ""
tmp = 2 ** i
for _ in range(idx):
    if order <= tmp // 2:
        ans += "4"
    else:
        ans += "7"
        order -= tmp // 2
    tmp //= 2

print(ans)