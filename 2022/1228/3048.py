N1, N2 = map(int, input().split())
G1 = input().rstrip()
G2 = input().rstrip()
T = int(input().rstrip())

order = []
for i in range(len(G1) - 1, -1, -1):
    order.append([G1[i], 1])
for i in range(len(G2)):
    order.append([G2[i], -1])

tmp = []
for t in range(T):
    for i in range(len(order) - 1):
        if order[i][1] == 1 and order[i + 1][1] == -1:
            tmp.append(i)
    for i in tmp:
        order[i], order[i + 1] = order[i + 1], order[i]
    tmp = []

ans = ''
for i in order:
    ans += i[0]
print(ans)