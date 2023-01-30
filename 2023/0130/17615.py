import sys
input = sys.stdin.readline

n = int(input())
strV = input().rstrip()
ans = float('inf')

start = strV[0]
end = strV[-1]

si = 0
for i in range(n):
    if strV[i] == start:
        si = i
    else:
        break
tmp = strV[si + 1:]
ans = min(ans, tmp.count("R"), tmp.count("B"))

ei = n - 1
for i in range(n - 1, -1, -1):
    if strV[i] == end:
        ei = i
    else:
        break

tmp = strV[:ei]
ans = min(ans, tmp.count("R"), tmp.count("B"))
print(ans)