N, L = map(int, input().split())
total = 0
cur = 0
for _ in range(N):
    D, R, G = map(int, input().split())
    total += D - cur
    cur = D
    if total % (R + G) <= R:
        total += R - total % (R + G)
total += L - cur
print(total)