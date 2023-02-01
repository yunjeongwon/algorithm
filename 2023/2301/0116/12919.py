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


# 거꾸로 푸는 풀이
import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def f(strV):
    global ans
    if strV == s:
        ans = 1
        return
    if len(strV) == 0:
        return
    if strV[-1] == "A":
        f(strV[:len(strV) - 1])
    if strV[0] == "B":
        f(strV[1:][::-1])

ans = 0
f(t)
print(ans)

