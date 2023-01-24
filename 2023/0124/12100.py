import copy
import sys
input = sys.stdin.readline

n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def f(v, board):
    global ans
    if v == 5:
        # for i in board:
        #     print(i)
        # print()
        for i in board:
            ans = max(ans, max(i))
        return

    tmp = copy.deepcopy(board)
    # 상
    for j in range(n):
        for i in range(n - 1):
            if tmp[i][j] == 0:
                continue
            ii = i + 1
            while ii < n:
                if tmp[ii][j] == 0:
                    ii += 1
                    continue
                else:
                    if tmp[ii][j] == tmp[i][j]:
                        tmp[i][j] += tmp[ii][j]
                        tmp[ii][j] = 0
                    break

        for i in range(n - 1):
            if tmp[i][j] != 0:
                continue
            ii = i + 1
            while ii < n:
                if tmp[ii][j] == 0:
                    ii += 1
                    continue
                else:
                    tmp[i][j] = tmp[ii][j]
                    tmp[ii][j] = 0
                    break

    f(v + 1, tmp)
    tmp = copy.deepcopy(board)

    # 하
    for j in range(n):
        for i in range(n - 1, 0, -1):
            if tmp[i][j] == 0:
                continue
            ii = i - 1
            while ii >= 0:
                if tmp[ii][j] == 0:
                    ii -= 1
                    continue
                else:
                    if tmp[ii][j] == tmp[i][j]:
                        tmp[i][j] += tmp[ii][j]
                        tmp[ii][j] = 0
                    break

        for i in range(n - 2, -1, -1):
            if tmp[i][j] == 0:
                continue
            ii = i
            while True:
                if ii + 1 < n and tmp[ii + 1][j] == 0:
                    tmp[ii + 1][j] = tmp[ii][j]
                    tmp[ii][j] = 0
                    ii += 1
                else:
                    break


    f(v + 1, tmp)
    tmp = copy.deepcopy(board)

    # 좌
    for i in range(n):
        for j in range(n - 1):
            if tmp[i][j] == 0:
                continue
            jj = j + 1
            while jj < n:
                if tmp[i][jj] == 0:
                    jj += 1
                    continue
                else:
                    if tmp[i][j] == tmp[i][jj]:
                        tmp[i][j] += tmp[i][jj]
                        tmp[i][jj] = 0
                    break

        for j in range(n - 1):
            if tmp[i][j] != 0:
                continue
            jj = j + 1
            while jj < n:
                if tmp[i][jj] == 0:
                    jj += 1
                    continue
                else:
                    tmp[i][j] = tmp[i][jj]
                    tmp[i][jj] = 0
                    break


    f(v + 1, tmp)
    tmp = copy.deepcopy(board)
    # 우
    for i in range(n):
        for j in range(n - 1, 0, -1):
            if tmp[i][j] == 0:
                continue
            jj = j - 1
            while jj >= 0:
                if tmp[i][jj] == 0:
                    jj -= 1
                    continue
                else:
                    if tmp[i][j] == tmp[i][jj]:
                        tmp[i][j] += tmp[i][jj]
                        tmp[i][jj] = 0
                    break
        for j in range(n - 1, 0, -1):
            if tmp[i][j] != 0:
                continue
            jj = j - 1
            while jj >= 0:
                if tmp[i][jj] == 0:
                    jj -= 1
                    continue
                else:
                    tmp[i][j] = tmp[i][jj]
                    tmp[i][jj] = 0
                    break

    f(v + 1, tmp)

f(0, G)
print(ans)
