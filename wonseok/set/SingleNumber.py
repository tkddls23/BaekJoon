# single number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        double_nums = list(set(nums))*2

        for num in nums:
            double_nums.remove(num)

        return double_nums[0]