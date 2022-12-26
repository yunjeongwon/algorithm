import math
def solution(num, total):
    answer = []
    a = math.ceil(total / num)
    for i in range(a - num // 2, a - num // 2 + num):
        answer.append(i)
    return answer