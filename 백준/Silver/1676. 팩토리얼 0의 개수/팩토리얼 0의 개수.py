import sys
input = sys.stdin.readline

n = int(input())

tmp = 1
for i in range(2, n + 1):
    tmp *= i
tmp = str(tmp)[::-1]

ans = 0
for i in range(len(tmp)):
    if tmp[i] == "0":
        ans += 1
    else:
        break
print(ans)