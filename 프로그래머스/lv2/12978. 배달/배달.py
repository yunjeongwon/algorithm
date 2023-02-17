from heapq import heappush, heappop

def f(s, g, dist):
    qu = []
    heappush(qu, [0, s])
    dist[s] = 0
    while qu:
        cur_dist, cur_node = heappop(qu)

        if cur_dist > dist[cur_node]:
            continue

        for new_dist, new_node in g[cur_node]:
            if dist[new_node] > new_dist + cur_dist:
                dist[new_node] = new_dist + cur_dist
                heappush(qu, [new_dist + cur_dist, new_node])

def solution(N, road, K):
    ans = 0
    g = [[] for _ in range(N + 1)]
    INF = float('inf')
    dist = [INF] * (N + 1)
    for a, b, c in road:
        g[a].append([c, b])
        g[b].append([c, a])
    f(1, g, dist)
    for i in dist:
        if i <= K:
            ans += 1
    return ans