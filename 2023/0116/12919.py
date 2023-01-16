import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def f(strV):
    global ans
    if len(strV) == len(t):
        return
    flag = 0
    for i in range(len(t) - len(strV) + 1):
        tmp = t[i:i + len(strV)]
        if tmp == strV or tmp == strV[::-1]:
            flag = 1
    if flag == 0:
        return
    res = strV + "A"
    if res == t:
        ans = 1
        return
    else:
        f(res)

    res = strV + "B"
    res = res[::-1]

    if res == t:
        ans = 1
        return
    else:
        f(res)

ans = 0
f(s)
print(ans)
