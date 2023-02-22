import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

p = 'I'
for _ in range(n):
    p += 'OI'
ans = 0
l = 0
r = len(p)
while l < m - len(p) + 1:
    if s[l:r] == p:
        ans += 1
        l += 2
        r += 2
    else:
        l += 1
        r += 1

print(ans)
