# Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums = list(set(nums))
        dic_nums = {}
        for set_num in set_nums:
            dic_nums[set_num] = nums.count(set_num)
        for i in dic_nums:
            if dic_nums[i] > (len(nums) / 2):
                return i