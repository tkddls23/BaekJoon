def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total_dates = -1
    
    for i in range(a-1):
        total_dates += dates[i]
    total_dates += b
    
    print(total_dates%7)
    return days[total_dates%7]
    
    