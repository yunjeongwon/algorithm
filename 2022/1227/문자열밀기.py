def solution(A, B):
    answer = 0
    n = len(A)
    while A != B:
        A = A[-1] + A[:-1]
        answer += 1
        if answer >= len(A):
            return -1
    return answer