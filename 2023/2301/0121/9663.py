import sys
input = sys.stdin.readline

n = int(input())

def check(cr):
    for i in range(cr):
        if col[cr] == col[i]:
            return False
        if abs(cr - i) == abs(col[cr] - col[i]):
            return False
    return True

def f(cr):
    global ans
    if cr == n:
        ans += 1
        return

    for cc in range(n):
        col[cr] = cc
        if check(cr):
            f(cr + 1)

ans = 0
col = [0] * n
f(0)
print(ans)