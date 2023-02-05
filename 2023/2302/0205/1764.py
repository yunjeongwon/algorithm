import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = [input().rstrip() for _ in range(n)]
arr2 = [input().rstrip() for _ in range(m)]
arr1.sort()
arr2.sort()
l = 0
r = 0
ans = []
while l < n and r < m:
    if arr1[l] == arr2[r]:
        ans.append(arr1[l])
        l += 1
        r += 1
    elif arr1[l] < arr2[r]:
        l += 1
    elif arr1[l] > arr2[r]:
        r += 1

print(len(ans))
for i in ans:
    print(i)