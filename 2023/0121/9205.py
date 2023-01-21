import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    # 편의점 개수
    n = int(input())
    sr, sc = map(int, input().split())
    conv = [list(map(int, input().split())) for _ in range(n)]
    visited = []
    er, ec = map(int, input().split())
    conv.append([er, ec])

    def bfs():
        qu = deque()
        qu.append([sr, sc])
        while qu:
            cr, cc = qu.popleft()

            for nr, nc in conv:
                dist = abs(cr - nr) + abs(cc - nc)
                if dist <= 1000 and [nr, nc] not in visited:
                    if nr == er and nc == ec:
                        return "happy"
                    qu.append([nr, nc])
                    visited.append([nr, nc])
        return "sad"

    ans = bfs()
    print(ans)
