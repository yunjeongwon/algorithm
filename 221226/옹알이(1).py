from itertools import permutations


def solution(babbling):
    pro = ["aya", "ye", "woo", "ma"]
    answer = 0
    word = []
    for i in range(1, len(pro) + 1):
        for k in permutations(pro, i):
            word.append(''.join(k))
    for b in babbling:
        if b in word:
            answer += 1 
    return answer
