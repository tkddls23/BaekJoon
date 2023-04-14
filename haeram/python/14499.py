from sys import stdin

n, m, x, y, k = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

com = list(map(int, stdin.readline().split()))