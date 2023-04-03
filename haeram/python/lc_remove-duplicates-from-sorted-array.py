class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()

        cand = []
        for i in range(len(nums)):
            if(nums[i] in s):
                cand.append(i)
            else:
                s.add(nums[i])

        for i in range(len(cand)):
            del nums[cand[i] - i]
            

        return len(s)