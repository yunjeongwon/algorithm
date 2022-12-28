G = [list(input().split()) for _ in range(3)]

for i in range(3):
    res = 0
    for k in range(4):
        if G[i][k] == '0':
            res += 1
    if res == 1:
        print('A')
    elif res == 2:
        print('B')
    elif res == 3:
        print('C')
    elif res == 4:
        print('D')
    elif res == 0:
        print('E')