from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    age, name = stdin.readline().split()
    age = int(age)

    arr.append((age, name))

sort_age = sorted(arr, key = lambda x: x[0])

for i in sort_age:
    print(i[0], i[1])