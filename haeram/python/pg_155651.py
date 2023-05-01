def is_after(t1, t2):
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    
    if h1*60 + m1 + 10 <= h2*60 + m2:
        return True
    else:
        return False
    

def solution(book_time):
    book_time.sort(key=lambda x: x[0])
    
    rooms = {}
    room_cnt = 0
    
    for book in book_time:
        start, end = book[0], book[1]
        
        new_room = True
        for room in rooms.keys():
            if is_after(rooms[room], start):
                new_room = False
                rooms[room] = end
                break
                
        if new_room:
            rooms[room_cnt] = end
            room_cnt += 1
        
    return room_cnt
        
    