import sys
input = sys.stdin.readline

n = int(input())
given = ""
for _ in range(n):
    given += input().rstrip()

l = 0
r = n - 1
ans = ""
while l <= r:
    if l == r:
        ans += given[l]
        break
    if given[l] > given[r]:
        ans += given[r]
        r -= 1
    elif given[l] < given[r]:
        ans += given[l]
        l += 1
    else:
        tmp = (r - l - 1) // 2
        flag = False
        for i in range(1, tmp + 1):
            if given[l + i] == given[r - i]:
                continue
            if given[l + i] < given[r - i]:
                ans += given[l]
                l += 1
                flag = True
                break
            if given[l + i] > given[r - i]:
                ans += given[r]
                r -= 1
                flag = True
                break
        if not flag:
            ans += given[l]
            l += 1

l = len(ans)
mok = l // 80
na = l % 80
for i in range(mok):
    print(ans[i * 80:i * 80 + 80])
print(ans[mok * 80: mok * 80 + na])
