from sys import stdin

t = int(stdin.readline().rstrip())

ans = []
for _ in range(t):
    cards = list(map(float, stdin.readline().split()))
    num = cards.pop(0)
    times = cards.pop(0)

    

