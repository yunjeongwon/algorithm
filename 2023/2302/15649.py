import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def f(v, arr):
    if v == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            f(v + 1, arr + [i])
            visited[i] = 0

visited = [0] * (n + 1)
f(0, [])