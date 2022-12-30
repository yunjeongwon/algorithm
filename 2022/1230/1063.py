K, D, N = input().split()
N = int(N)
G = [[0] * 8 for _ in range(8)]
dict = { "R" : [0, 1], "L" : [0, -1], "B" : [1, 0], "T" : [-1, 0], "RT" : [1, -1], "LT" : [-1, -1], "RB" : [1, 1], "LB" : [1, -1] }

def f(strV, n):
    a1, a2 = strV
    a2 = int(a2)
    a1 = ord(a1) - ord("A")
    a2 = 8 - a2
    G[a2][a1] = n
f(K, 1)
f(D, 2)

def find(curD):
    for cr in range(8):
        for cc in range(8):
            if G[cr][cc] == 1:
                dr, dc = dict[curD]
                nr, nc = cr + dr, cc + dc
                if nr >= 8 or nr < 0 or nc >= 8 or nc < 0:
                    return
                if G[nr][nc] == 2:
                    if nr + dr >= 8 or nr + dr < 0 or nc + dc >= 8 or nc + dc < 0:
                        return
                    G[nr + dr][nc + dc] = 2
                G[cr][cc] = 0
                G[nr][nc] = 1
                return

for _ in range(N):
    curD = input().rstrip()
    find(curD)
# print(G)
def re(n):
    for i in range(8):
        for k in range(8):
            if G[i][k] == n:
                cr = 8 - i
                cc = chr(k + ord("A"))
                return cc + str(cr)
print(re(1))
print(re(2))
