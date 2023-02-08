import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def dfs(cr, cc, size, sumV):
    if size == 0:
        print(sumV)
        return
    tmp = (size // 2) ** 2
    size //= 2
    if cr < size and cc < size:
        dfs(cr, cc, size, sumV + tmp * 0)
    if cr < size and cc >= size:
        dfs(cr, cc - size, size, sumV + tmp * 1)
    if cr >= size and cc < size:
        dfs(cr - size, cc, size, sumV + tmp * 2)
    if cr >= size and cc >= size:
        dfs(cr - size, cc - size, size, sumV + tmp * 3)

dfs(r, c, 2 ** n, 0)
