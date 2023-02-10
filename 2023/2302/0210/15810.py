import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
r = min(arr) * m - 1
while l <= r:
    midTime = (l + r) // 2
    res = 0
    for i in arr:
        res += midTime // i
    if res < m:
        l = midTime + 1
    else:
        r = midTime - 1
print(l)