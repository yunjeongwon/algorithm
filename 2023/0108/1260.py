import sys
input = sys.stdin.readline
from collections import deque


N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in G:
    i.sort()

def dfs(c):
    visited[c] = 1
    print(c, end=" ")
    for new in G[c]:
        if visited[new] == 0:
            dfs(new)

visited = [0] * (N + 1)
dfs(V)
print()
def bfs(s):
    qu = deque()
    visited = [0] * (N + 1)
    qu.append(s)
    visited[s] = 1
    print(s, end=" ")
    while qu:
        cur = qu.popleft()

        for new in G[cur]:
            if visited[new] == 0:
                visited[new] = 1
                qu.append(new)
                print(new, end=" ")
bfs(V)
print()