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


# 시간초과난 백트래킹 코드
# import sys
# input = sys.stdin.readline

# n = int(input())
# G = [list(map(int, input().split())) for _ in range(n)]
# ans = int(1e9)

# def cal(arr1, arr2):
#     sum1 = 0
#     sum2 = 0
#     for i in range(n // 2):
#         for j in range(n // 2):
#             sum1 += G[arr1[i]][arr1[j]]
#             sum2 += G[arr2[i]][arr2[j]]
#     return abs(sum1 - sum2)

# def f(v, arr):
#     global ans
#     if v == n // 2:
#         tmp = []
#         for i in range(n):
#             if i not in arr:
#                 tmp.append(i)
#         ans = min(ans, cal(arr, tmp))
#         return

#     for i in range(v, n):
#         if i not in arr:
#             f(v + 1, arr + [i])

# f(0, [])
# print(ans)
