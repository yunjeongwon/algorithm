import sys
input = sys.stdin.readline
from itertools import combinations

def dfs(r):
    global ans
    if r == 15:
        ans = 1
        for s in scores:
            if s.count(0) != 3:
                ans = 0
                break
        return

    t1, t2 = games[r]
    # 승패, 무무, 패승
    for res1, res2 in ((0, 2), (1, 1), (2, 0)):
        if scores[t1][res1] > 0 and scores[t2][res2] > 0:
            scores[t1][res1] -= 1
            scores[t2][res2] -= 1
            dfs(r + 1)
            scores[t1][res1] += 1
            scores[t2][res2] += 1

for _ in range(4):
    arr = list(map(int, input().split()))
    scores = []
    for i in range(6):
        a, b, c = arr[i * 3:i * 3 + 3]
        scores.append([a, b, c])
    games = list(combinations(range(6), 2))
    ans = 0
    dfs(0)
    print(ans, end=" ")
print()
