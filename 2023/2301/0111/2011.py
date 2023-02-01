import sys
input = sys.stdin.readline

N = input().rstrip()
L = len(N)
if N[0] == "0":
    print(0)
    exit()
arr = []
for i in range(L - 1):
    if N[i] == "0":
        if N[i + 1] == "0":
            print(0)
            exit()
        continue
    if N[i + 1] == "0":
        arr.append(N[i] + N[i + 1])
    else:
        arr.append(N[i])
if N[-1] != "0":
    arr.append(N[-1])
for i in arr:
    tmp = int(i)
    if tmp > 26:
        print(0)
        exit()
dp = [0] * len(arr)
dp[0] = 1

for i in range(1, len(arr)):
    if len(arr[i]) == 2:
        dp[i] = dp[i - 1]
    else:
        temp = arr[i - 1] + arr[i]
        if int(temp) <= 26:
            if i == 1:
                dp[1] = (dp[i - 1] + 1)
            else:
                dp[i] = (dp[i - 2] + dp[i - 1])
        else:
            dp[i] = dp[i - 1]

print(dp[len(arr) - 1] % 1000000)
