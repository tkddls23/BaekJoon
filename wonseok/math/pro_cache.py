def solution(cacheSize, cities):
    cache = []
    answer = 0
    if len(cacheSize) == 0:
        return len(cities) * 5
    for city in cities:
        if city.upper() in cache:
            answer += 1
            cache.remove(city.upper())
            cache.append(city.upper())
        else:
            answer += 5
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city.upper())

    return answer

# maxlen?
# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5
#     return time