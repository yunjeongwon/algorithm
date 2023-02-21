import sys
input = sys.stdin.readline

given = list(input().rstrip())
cntA = given.count('a')
n = len(given)
ans = n
for i in range(cntA - 1):
    given += given[i]

for i in range(n):
    tmp = given[i:i + cntA].count('b')
    ans = min(ans, tmp)
print(ans)