import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
K = int(input())
ans = 0

def dfs(num):
    arr[num] = -2
    for i in range(N):
        if arr[i] == num:
            dfs(i)

dfs(K)

for i in range(N):
    if i not in arr and arr[i] != -2:
        ans += 1
print(ans)