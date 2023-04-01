def solution(phone_book):
    phone_book.sort()
    
    ans = True
    
    for i in range(1, len(phone_book)):
        prev = min(len(phone_book[i-1]), len(phone_book[i]))
        if(phone_book[i-1] == phone_book[i][:prev]):
            ans = False
            break
            
    return ans