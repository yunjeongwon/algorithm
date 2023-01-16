import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m, x = map(int, input().split())
G1 = [[] for _ in range(n + 1)]
G2 = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    G1[a].append([t, b])
    G2[b].append([t, a])

def d(s, G):
    time = [float('inf')] * (n + 1)
    time[s] = 0
    qu = []
    visited = [0] * (n + 1)
    heappush(qu, [0, s])
    visited[s] = 1
    while qu:
        cur_time, cur_node = heappop(qu)

        if time[cur_node] < cur_time:
            continue

        for new_time, new_node in G[cur_node]:
            if time[new_node] > cur_time + new_time:
                time[new_node] = cur_time + new_time
                heappush(qu, [cur_time + new_time, new_node])
    return time

ans = 0
res1 = d(x, G1)
res2 = d(x, G2)
for i in range(1, n + 1):
    ans = max(ans, res1[i] + res2[i])
print(ans)