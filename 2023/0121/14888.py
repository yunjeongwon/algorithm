import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

maxV = - 10 ** 9
minV = 10 ** 9

def f(v, res, cand):
    global maxV, minV
    if v == n:
        maxV = max(maxV, res)
        minV = min(minV, res)
        return

    for i in range(4):
        if cand[i] != 0:
            tmp = cand[:]
            tmp[i] -= 1
            if i == 0:
                f(v + 1, res + arr[v], tmp)
            elif i == 1:
                f(v + 1, res - arr[v], tmp)
            elif i == 2:
                f(v + 1, res * arr[v], tmp)
            else:
                if res < 0 and arr[v] > 0:
                    res *= -1
                    f(v + 1, res // arr[v] * -1, tmp)
                else:
                    f(v + 1, res // arr[v], tmp)

f(1, arr[0], op)
print(maxV)
print(minV)