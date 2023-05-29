import sys
input = sys.stdin.readline

n = int(input())
my = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

my = sorted(my)

ans = [0] * m

for i in range(m):
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2

        if arr[i] > my[mid]:
            l = mid + 1
        elif arr[i] < my[mid]:
            r = mid - 1
        else:
            ans[i] = 1
            break
print(*ans)