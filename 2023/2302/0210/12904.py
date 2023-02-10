import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

s = input().rstrip()
t = input().rstrip()
ans = 0

tmp = t
for _ in range(len(t) - len(s)):
    if tmp[-1] == "A":
        tmp = tmp[:len(tmp) - 1]
    elif tmp[-1] == "B":
        tmp = tmp[:len(tmp) - 1][::-1]

if tmp == s:
    ans = 1

print(ans)