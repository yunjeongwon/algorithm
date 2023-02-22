import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

p = 'I'
for _ in range(n):
    p += 'OI'

ans = 0
cnt = 0
i = 0
while i < m - 1:
    if s[i: i + 3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(ans)