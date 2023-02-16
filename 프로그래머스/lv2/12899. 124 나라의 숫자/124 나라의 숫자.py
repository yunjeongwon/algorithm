def solution(n):
    ans = ''
    arr = [0] * 30
    for i in range(1, 30):
        arr[i] = arr[i - 1] + 3 ** i

    idx = -1
    for i in range(1, 30):
        if arr[i] >= n:
            idx = i
            break
    order = n - arr[idx - 1]


    tmp = 3 ** i
    for _ in range(idx):
        if order <= tmp // 3:
            ans += "1"
        elif order <= tmp // 3 * 2:
            ans += "2"
            order -= tmp // 3
        else:
            ans += "4"
            order -= tmp // 3 * 2
        tmp //= 3
    return ans