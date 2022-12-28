def solution(my_string):
    answer = ''
    lst = list(my_string)
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
    lst.sort()
    return ''.join(lst)
    