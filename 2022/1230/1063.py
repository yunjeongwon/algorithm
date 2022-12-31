dic = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
king, stone, N = input().rstrip().split()
N = int(N)
k = list(map(int, [ord(king[0]) - ord("A") + 1, king[1]]))
s = list(map(int, [ord(stone[0]) - ord("A") + 1, stone[1]]))
for _ in range(N):
    d = input().rstrip()
    nx = k[0] + dic[d][0]
    ny = k[1] + dic[d][1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        if nx == s[0] and ny == s[1]:
            nnx = s[0] + dic[d][0]
            nny = s[1] + dic[d][1]
            if 1 <= nnx <= 8 and 1 <= nny <= 8:
                k = [nx, ny]
                s = [nnx, nny]
        else:
            k = [nx, ny]

print(f'{chr(k[0] + ord("A") - 1)}{k[1]}')
print(f'{chr(s[0] + ord("A") - 1)}{s[1]}')