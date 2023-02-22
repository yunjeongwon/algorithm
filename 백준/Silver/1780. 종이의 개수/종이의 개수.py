import sys
input = sys.stdin.readline

n = int(input().rstrip())
g = [list(map(int, input().split())) for _ in range(n)]
ans1 = ans2 = ans3 = 0

def f(sr, sc, size):
    global ans1, ans2, ans3
    cnt1 = cnt2 = cnt3 = 0
    for cr in range(sr, sr + size):
        for cc in range(sc, sc + size):
            if g[cr][cc] == -1:
                cnt1 += 1
            elif g[cr][cc] == 0:
                cnt2 += 1
            else:
                cnt3 += 1
    if cnt1 == 0 and cnt2 == 0:
        ans3 += 1
    elif cnt2 == 0 and cnt3 == 0:
        ans1 += 1
    elif cnt3 == 0 and cnt1 == 0:
        ans2 += 1
    else:
        for i in range(3):
            for j in range(3):
                f(sr + size // 3 * i, sc + size // 3 * j, size // 3)

f(0, 0, n)

print(ans1)
print(ans2)
print(ans3)
