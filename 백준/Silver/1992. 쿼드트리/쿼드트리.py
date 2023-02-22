import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().rstrip())) for _ in range(n)]
def f(sr, sc, size):
    cnt0 = cnt1 = 0
    for cr in range(sr, sr + size):
        for cc in range(sc, sc + size):
            if g[cr][cc] == 0:
                cnt0 += 1
            else:
                cnt1 += 1
    if cnt0 == 0:
        print(1, end='')
    elif cnt1 == 0:
        print(0, end='')
    else:
        print('(', end='')
        for i in range(2):
            for j in range(2):
                f(sr + size // 2 * i, sc + size // 2 * j, size // 2)
        print(')', end='')

f(0, 0, n)
