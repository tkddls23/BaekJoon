from queue import PriorityQueue


def solution(n, k, enemys):
    PQ = PriorityQueue()
    round = 0
    for enemy in enemys:
        PQ.put(enemy * -1)
        n -= enemy
        if n < 0:
            if k <= 0:
                return round
            k -= 1
            n += PQ.get() * -1
        round += 1
    return round