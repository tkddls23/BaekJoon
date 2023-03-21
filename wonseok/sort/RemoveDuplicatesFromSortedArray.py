# Remove Duplicates From Sorted Array
class Solution:
    def removeDuplicates(self, nums):
        set_length = len(list(set(nums)))
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                nums[i] = 101
            i += 1

        nums.sort()
        return set_length

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))