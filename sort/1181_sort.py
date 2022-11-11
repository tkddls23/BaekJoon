# 1181 단어 정렬
import sys
word = []
n = int(sys.stdin.readline())
for i in range(n):
    word.append(input())

word = list(set(word))
word.sort()
word.sort(key=len)

for i in word:
    print(i)