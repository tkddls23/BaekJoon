def solution(s):
    s_to_list = list(s)
    s_to_list.sort(reverse=True)
    return "".join(s_to_list)

def solution2(s):
    return "".join(sorted(s, reverse=True))