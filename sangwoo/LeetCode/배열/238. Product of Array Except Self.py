from collections import deque
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = deque(nums)

        mult = 1
        right = []
        result = []
        left = 1
        for i in range(len(d) - 1, 0, -1):
            mult *= d[i]
            right.append(mult)

        index = -1

        while len(d) > 1:
            itself = d.popleft()
            result.append(left * right[index])
            index -= 1
            left *= itself

        result.append(left)
        return result