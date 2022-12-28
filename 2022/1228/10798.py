G = [input().rstrip() for _ in range(5)]
ans = ''
for i in range(15):
    for k in range(5):
        if len(G[k]) > i:
            ans += G[k][i]
print(ans)
