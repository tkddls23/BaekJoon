def solution(book_time):
    room = 0
    for i in range(len(book_time)):
        it = list(map(int, book_time[i][0].split(':')))
        et = list(map(int, book_time[i][1].split(':')))
        book_time[i] = [it[0]*60 + it[1], et[0]*60 + et[1]]
    book_time.sort()
    while book_time:
        room += 1
        std = book_time.pop(0)
        for book in book_time[:]:
            if book[0] >= std[1]+10: 
                book_time.remove(book)
                std = book
    return room