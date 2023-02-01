import sys
input = sys.stdin.readline

n, k = map(int, input().split())
given = []
remain = []
for i in range(ord('a'), ord('z') + 1):
    if chr(i) in 'antic':
        continue
    remain.append(chr(i))
for _ in range(n):
    a = list(input().rstrip())
    a = list(set(a))
    tmp = ""
    for i in a:
        if i in 'antic':
            continue
        tmp += i
    given.append(''.join(tmp))
def f(v, strV):
    global ans
    if v == k - 5:
        res = 0
        for item in given:
            flag = True
            for charV in item:
                if charV not in strV:
                    flag = False
            if flag:
                res += 1
        ans = max(ans, res)
        return

    for i in range(len(remain)):
        if visited[i] == 0:
            if strV != "":
                if strV[-1] > remain[i]:
                    continue
            visited[i] = 1
            f(v + 1, strV + remain[i])
            visited[i] = 0

ans = 0
visited = [0] * len(remain)
if k - 5 >= 0:
    f(0, '')
print(ans)