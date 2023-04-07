# move zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0  # left 이상에서 0이아닌 수가 처음 장하는 index
        n = len(nums)

        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left] # left의 원소는 0일테니
                left += 1
            right += 1

        return nums