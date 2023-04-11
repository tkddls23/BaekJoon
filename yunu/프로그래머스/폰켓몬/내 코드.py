def solution(nums):
    uni = set(nums)
    
    return min(len(nums) / 2, len(uni))
