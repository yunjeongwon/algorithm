import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
while arr.count(0) != n:
    flag = True
    for i in range(n):
        if arr[i] % 2 != 0:
            flag = False

    if flag:
        for i in range(n):
            arr[i] //= 2
    else:
        for i in range(n):
            if arr[i] % 2 != 0:
                arr[i] -= 1
                break
    ans += 1

print(ans)