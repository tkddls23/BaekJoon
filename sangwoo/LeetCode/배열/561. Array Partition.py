from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         nums.sort()
#         max_sum = 0
#
#         for i in range(0, len(nums), 2):
#             max_sum += nums[i]
#
#         return max_sum

# 어떻게 이 풀이를 떠올렸지?
# 주어진 배열은 2n 개의 정수 배열이다.
# 정렬 한 후에 0, 2, 4... 번째 수만을 더하면 최대합을 구할 수 있다.

# 더 좋은 방법은?
# 슬라이싱 사용
