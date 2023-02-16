def solution(n):
    ans = ''
    cand = ["1", "2", "4"]
    ans = ""

    while n > 0:
        n -= 1
        ans = cand[n % 3] + ans
        n //= 3
    return ans