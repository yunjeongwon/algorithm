import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())

    ans = 1

    for i in range(m, m - n, -1):
        ans *= i

    for i in range(n, 0, -1):
        ans //= i

    print(ans)