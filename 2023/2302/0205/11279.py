import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
qu = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if not qu:
            print(0)
        else:
            print(-heappop(qu))
    else:
        heappush(qu, -x)
