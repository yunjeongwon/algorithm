import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    qu = deque()
    visited = [0] * (n + 1)
    qu.append(s)
    visited[s] = 1
    if G[s] == s:
        ans.append(s)
        return
    while qu:
        cur = qu.popleft()
        new = G[cur]
        if visited[new] == 0:
            visited[new] = 1
            qu.append(new)
            if G[new] == s:
                for i in range(1, n + 1):
                    if visited[i] == 1:
                        ans.append(i)
                return

n = int(input())
G = [0] + [int(input().rstrip()) for _ in range(n)]
ans = []

for i in range(1, n + 1):
    if i not in ans:
        bfs(i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)