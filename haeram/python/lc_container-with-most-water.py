# 이분탐색 : 정답 틀림 (높이 11 -> 10 돼야 하는 경우)

# def calc(h, arr): # 물 높이가 h일 때 계산
#     start = -1
#     end = -1

#     length = len(arr)
#     for i in range(length):
#         if(start != -1 and end != -1):
#             break
        
#         if(start == -1 and arr[i] >= h):
#             start = i

#         if(end == -1 and arr[length-1-i] >= h):
#             end = length-1-i

#     if(start >= end):
#         return -1
#     else:
#         print('calc', start, end, h, arr)
#         return (end-start) * h


# def pro(height):
#     temp = sorted(height)
#     left = temp[0]
#     right = temp[-1]

#     ans = 0

#     if left == right:
#         return left
    
#     #binary search
#     while left <= right:
#         mid = (left + right) // 2

#         cur_water = calc(mid, height)

#         print('it', left, right, cur_water)

#         if cur_water < ans:
#             right = mid - 1
#         else:
#             ans = cur_water
#             left = mid + 1


# -------------------------------------------------------------------#

# 투 포인터

def calc(start, end, arr): # 물 높이가 h일 때 계산
    if arr[start] < arr[end]:
        return (end-start)*arr[start]
    else:
        return (end-start)*arr[end]
    

def pro(height):
    length = len(height)

    start = 0
    end = length-1

    ans = calc(start, end, height)

    while start < end:
        cur_water = calc(start, end, height)

        if cur_water > ans:
            ans = cur_water

        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return ans
    
  
print(pro([1,8,6,2,5,4,8,3,7])) #49
print(pro([1,1])) #1
print(pro([4,3,2,1,4])) #16
print(pro([8,10,14,0,13,10,9,9,11,11])) #80

