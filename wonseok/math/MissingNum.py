# missing Num
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        gauss = n*(n+1)//2
        return gauss-sum(nums)