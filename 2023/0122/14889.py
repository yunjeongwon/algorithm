import sys
input = sys.stdin.readline
from itertools import combinations as cb

n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')
comb = list(cb(range(n), n // 2))

for c in comb:
    sum1 = 0
    for i in c:
        for j in c:
            sum1 += G[i][j]

    sum2 = 0
    for i in range(n):
        for j in range(n):
            if i not in c and j not in c:
                sum2 += G[i][j]

    diff = abs(sum1 - sum2)
    ans = min(ans, diff)
print(ans)