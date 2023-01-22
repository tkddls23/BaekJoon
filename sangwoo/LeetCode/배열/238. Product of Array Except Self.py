from collections import deque
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        multiplication_value = 1

        for i in range(0, len(nums)):
            result.append(multiplication_value)
            multiplication_value = multiplication_value * nums[i]

        multiplication_value = 1

        for i in range(len(nums) - 1, 0 - 1, -1):
            result[i] = result[i] * multiplication_value
            multiplication_value = multiplication_value * nums[i]
        return result

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         d = deque(nums)
#
#         mult = 1
#         right = []
#         result = []
#         left = 1
#         for i in range(len(d) - 1, 0, -1):
#             mult *= d[i]
#             right.append(mult)
#
#         index = -1
#
#         while len(d) > 1:
#             itself = d.popleft()
#             result.append(left * right[index])
#             index -= 1
#             left *= itself
#
#         result.append(left)
#         return result

# 풀이
# 자기를 제외한 곱을 구해야 하므로 while 반복문을 돌며 가장 앞 원소를 pop했다.
# 가장 앞 원소를 pop 해야 하므로 deque 자료형을 사용했다.
# 가장 앞 원소가 빠진 deque의 곱과 지금까지 pop된 값들의 곱을 서로 곱해주면 자신을 제외한 곱을 구할 수 있다.
# 가장 앞 원소가 빠진 deque의 곱은 right 리스트에 저장했다.
# 지금까지 pop된 값들의 곱은 left 변수에 저장했다.
