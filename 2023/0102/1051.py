N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N):
    for k in input().rstrip():
        G[i].append(int(k))

ans = 1
L = min(N, M) - 1
# 두께
for l in range(L + 1):
    # 시작점
    for sr in range(N - l):
        for sc in range(M - l):
            a = [sr, sc]
            b = [sr + l, sc]
            c = [sr, sc + l]
            d = [sr + l, sc + l]
            if G[sr][sc] == G[sr + l][sc] == G[sr][sc + l] == G[sr + l][sc + l]:
                ans = max(ans, (l + 1) ** 2)
print(ans)