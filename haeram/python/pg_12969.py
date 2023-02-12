from sys import stdin

n, m = map(int, stdin.readline().split())

for i in range(m):
    for j in range(n):
        print('*', end='')
    print()



# 다른 풀이
answer = ('*'*n + '\n')*m
print(answer)


# 다른 풀이 2
for _ in range(m):
    print('*'*n)