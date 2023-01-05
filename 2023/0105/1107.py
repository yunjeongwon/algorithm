N = int(input())
M = int(input())
minCnt = abs(N - 100)
if M == 0:
    arr = []
else:
    arr = input().rstrip().split()
for i in range(1000001):
    cur = str(i)
    l = len(cur)
    for k in range(l):
        if cur[k] in arr:
            break
        elif k == l - 1:
            diff = abs(N - i)
            if minCnt > diff + l:
                minCnt = diff + l
print(minCnt)