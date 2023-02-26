from sys import stdin

n, m = map(int, stdin.readline().split())
user = set(stdin.readline().split()[1:])
parties = []
cnt = 0

for _ in range(m):
    parties.append(set(stdin.readline().split()[1:]))

for _ in range(m):
    for party in parties:
        if party.intersection(user): # 진실을 아는사람이랑 같은 파티에 있다면
            user = user.union(party)

for party in parties:
    if not party.intersection(user): # 진실을 아는사람이 파티에 없다면
        cnt += 1


print(cnt)