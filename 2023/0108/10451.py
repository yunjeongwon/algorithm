import sys
input = sys.stdin.readline
from collections import deque

def f(s):
    qu = deque()
    qu.append(s)
    visited[s] = 1
    while qu:
        cur = qu.popleft()

        for new in G[cur]:
            if visited[new] == 0:
                visited[new] = 1
                qu.append(new)

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        G[i].append(arr[i])
    ans = 0
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        if visited[i] == 0:
            f(i)
            ans += 1
    print(ans)