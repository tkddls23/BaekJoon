reverse_map = {
    'd': 'u',
    'l': 'r',
    'r': 'l',
    'u': 'd'
}


def solution(n, m, x, y, r, c, k):

    x -= 1
    y -= 1
    r -= 1
    c -= 1

    x, y = y, x
    r, c = c, r

    answer = ''
    dic = {
        'd': 0,
        'l': 0,
        'r': 0,
        'u': 0,
        'share': 0
    }

    up_down = y - c
    left_right = x - r
    if k < abs(up_down) + abs(left_right) or (k - abs(up_down) - abs(left_right)) % 2 != 0:
        return "impossible"
    init(dic, k, left_right, up_down)

    while break_condition(dic):
        can_use = ['d', 'l', 'r', 'u']
        if y + 1 >= n:
            can_use.remove('d')
        if y <= 0:
            can_use.remove('u')
        if x + 1 >= m:
            can_use.remove('r')
        if x <= 0:
            can_use.remove('l')

        for i in can_use:
            global reverse_map
            if dic[i] == 0 and dic['share'] > 0:
                dic['share'] -= 1
                dic[reverse_map[i]] += 1
                x, y = increase_or_decrease_index(i, x, y)
                answer += i
                break
            if dic[i] != 0:
                answer += i
                dic[i] -= 1
                x, y = increase_or_decrease_index(i, x, y)
                break

    return answer


def increase_or_decrease_index(char, x, y) :
    if char == 'd' :
        y += 1
    elif char == 'u' :
        y -= 1
    elif char == 'l' :
        x -= 1
    else:
        x += 1
    return x, y

def break_condition(dic):
    sum = 0
    for key, value in dic.items():
        sum += value
    if sum == 0:
        return False
    return True


def init(dic, k, left_right, up_down):
    if up_down > 0:
        for i in range(up_down):
            dic['u'] += 1
    else:
        for i in range(abs(up_down)):
            dic['d'] += 1
    if left_right > 0:
        for i in range(left_right):
            dic['l'] += 1
    else:
        for i in range(abs(left_right)):
            dic['r'] += 1
    share = (k - abs(up_down) - abs(left_right)) // 2
    dic['share'] = share


print(solution(3, 4, 2, 3, 3, 1, 5))

print(solution(3, 4, 2, 1, 3, 3, 5))
