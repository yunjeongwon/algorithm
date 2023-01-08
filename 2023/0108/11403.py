import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1 or (G[i][k] == 1 and G[k][j] == 1):
                G[i][j] = 1
for i in range(N):
    for j in range(N):
        print(G[i][j], end=" ")
    print()