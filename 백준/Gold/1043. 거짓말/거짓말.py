import sys
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())
a = list(map(int, input().split()))
total = a[0]
knownPeople = a[1:]

G = [[0] * (n + 1) for _ in range(n + 1)]
parties = []

for _ in range(m):
    a = list(map(int, input().split()))
    personnel = a[0]
    participantList = a[1:]

    parties.append(participantList)

    for i in participantList:
        for j in participantList:
            G[i][j] = 1


def f(v):
    qu = deque()
    qu.append(v)
    visited[v] = 1

    while qu:
        c = qu.popleft()

        for i in range(1, n + 1):
            if G[c][i] == 1 and visited[i] == 0:
                visited[i] = 1
                qu.append(i)

visited = [0] * (n + 1)
for i in knownPeople:
    f(i)

ans = 0

for partyList in parties:
    flag = True
    for p in partyList:
        if visited[p] == 1:
            flag = False
            continue

    if flag:
        ans += 1

print(ans)