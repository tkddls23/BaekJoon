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

# 풀이
# result 리스트에 왼쪽부터 오른쪽으로 누적곱을 저장한다.
# 예를 들어 입력이 [1,2,3,4] 라면 [1,1,2,6]이 저장된다.
# 이를 이용해서 1 * 1을 제외한 2,3,4의 곱, 2를 제외한 1과 3,4의 곱 등으로 정답을 구할 수 있다.
# result 리스트를 반대로 for문을 돌며 1부터 시작해서 오른쪽에서 왼쪽으로 누적곱을 곱해준다.
# 6은 (1*2*3)으로 6*1으로 4를 제외한 값을 구하고 2는 (1*2) 이므로 2*1*4 으로 3을 제외한 값을 구할 수 있다.

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
