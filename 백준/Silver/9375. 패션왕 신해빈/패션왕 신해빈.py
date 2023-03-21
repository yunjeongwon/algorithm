import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    # if n == 0:
    #     print(0)
    #     exit()
    dic = {}
    for _ in range(n):
        cloth, kind = input().split()

        if kind in dic:
            dic[kind].append(cloth)
        else:
            dic[kind] = [cloth]

    ans = 1

    for i in dic:
        ans *= len(dic[i]) + 1

    ans -= 1

    print(ans)