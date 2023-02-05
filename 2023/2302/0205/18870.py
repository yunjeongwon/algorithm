import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sortedArr = sorted(set(arr))

dic = {}

for i in range(len(sortedArr)):
    dic[sortedArr[i]] = i

for i in arr:
    print(dic[i], end=" ")
print()