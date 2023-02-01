import sys
input = sys.stdin.readline
from itertools import permutations

A, B = input().rstrip().split()
res = list(permutations(A, len(A)))
B = int(B)
ans = -1
for r in res:
    a = int(''.join(map(str, r)))
    if len(str(a)) != len(r):
        continue
    if a < B:
        ans = max(ans, a)

print(ans)