import sys
from itertools import combinations

sys.stdin = open('index.txt')
input = sys.stdin.readline

def count_read_word(words,teach_word):
    cnt = 0
    for word in words:
        isRead=True
        for x in list(word):
            if x not in teach_word:
                isRead = False
                break
        if isRead:
            cnt+=1
    return cnt

def solution(k, arr):
    st = {'a', 'n', 't', 'a', 't', 'i', 'c', 'a'}
    remain_alphabet = set(chr(i) for i in range(97, 123)) - st

    if k < len(st):
        return 0
    cnt = 0
    for teach_words in list(combinations(remain_alphabet, k-len(st))):
        teach_word = st.union(teach_words)
        cnt = max(cnt, count_read_word(arr,teach_word))

    return cnt


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr =  [input().rstrip()[4:-4] for _ in range(n)]

    res = solution(k, arr)
    print(res)
