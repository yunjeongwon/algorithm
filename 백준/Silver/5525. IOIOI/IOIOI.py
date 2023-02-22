import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

p = 'I'
for _ in range(n):
    p += 'OI'

ans = 0
i = 0
while i < m - len(p) + 1:
    for j in range(len(p)):
        if s[i + j] != p[j]:
            i += 1
            break
    else:
        ans += 1
        i += 2

print(ans)