import sys
input = sys.stdin.readline

arr = list(input().rstrip())

arr = sorted(arr, reverse=True)

print(''.join(arr))