import sys
input = sys.stdin.readline

given = input().rstrip().split("-")
arr = []
for item in given:
    res = 0
    tmp = ""
    for i in item:
        if i.isdigit():
            tmp += i
        else:
            res += int(tmp)
            tmp = ""
    res += int(tmp)
    arr.append(res)


if len(arr) > 1:
    ans = arr[0]
    for i in range(1, len(arr)):
        ans -= arr[i]
    print(ans)
else:
    print(arr[0])