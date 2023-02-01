N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
ans = 0
for i in range(len(arr)):
    if arr[i][0] == K:
        ans = i
        break
for i in range(len(arr)):
    if arr[ans][1:] == arr[i][1:]:
        ans = i
        break

print(ans + 1)