import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for cr in range(N):
    for cc in range(1, N):
        nr, nc = cr, cc + 1
        if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == 0:
            dp[nr][nc][0] = dp[cr][cc][0] + dp[cr][cc][2]

        nr, nc = cr + 1, cc
        if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == 0:
            dp[nr][nc][1] = dp[cr][cc][1] + dp[cr][cc][2]

        nr, nc = cr + 1, cc + 1
        if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == 0 and G[nr - 1][nc] == 0 and G[nr][nc - 1] == 0:
            dp[nr][nc][2] = dp[cr][cc][0] + dp[cr][cc][1] + dp[cr][cc][2]


print(sum(dp[N - 1][N - 1]))

