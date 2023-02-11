import sys
input = sys.stdin.readline

arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2
arr[6] = 3

for i in range(7, 101):
    arr[i] = arr[i - 5] + arr[i - 1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(arr[n])