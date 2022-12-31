G = [[0] * 100 for _ in range(100)]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for k in range(b, b + 10):
            G[i][k] = 1
ans = 0
for i in range(100):
    for k in range(100):
        if G[i][k] == 1:
            ans += 1
print(ans)