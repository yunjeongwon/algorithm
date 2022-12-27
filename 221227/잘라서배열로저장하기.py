import math 

def solution(my_str, n):
    answer = []
    m = math.ceil(len(my_str) / n)
    for i in range(m - 1):
        answer.append(my_str[i * n:i * n + n])
    m -= 1
    answer.append(my_str[m * n:m * n + n])
    return answer