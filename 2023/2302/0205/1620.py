import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for i in range(1, n + 1):
    a = input().rstrip()
    dic[str(i)] = a
    dic[a] = i

for _ in range(m):
    a = input().rstrip()
    print(dic[a])