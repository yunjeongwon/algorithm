def solution(M, N):
    answer = 0
    answer += M - 1
    for _ in range(M):
        answer += N - 1
    return answer