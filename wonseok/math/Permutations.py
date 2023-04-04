from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list(permutations(nums,len(nums)))
        return result