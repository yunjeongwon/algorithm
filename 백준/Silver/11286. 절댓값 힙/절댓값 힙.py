import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
qu = []
for _ in range(n):
    x = int(input().rstrip())

    if x != 0:
        heappush(qu, [abs(x), x])
        continue
    if not len(qu):
        print(0)
        continue
    absed, origin = heappop(qu)

    print(origin)
