import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(m)]

l = 1
r = max(arr)
ans = 0
while l <= r:
    mid = (l + r) // 2
    tmp = m
    for i in arr:
        mok = math.ceil(i / mid) - 1
        tmp += mok

    if tmp > n:
        l = mid + 1
    else:
        r = mid - 1

print(l)