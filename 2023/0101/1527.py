import sys
input = sys.stdin.readline
from itertools import product

ans = 0
A, B = map(int, input().split())
arr = []
for i in range(len(str(A)), len(str(B)) + 1):
    arr = list(product([4, 7], repeat=i))
    for i in arr:
        tmp = int(''.join(map(str, i)))
        if A <= tmp <= B:
            ans += 1
print(ans)