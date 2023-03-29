# merged sorted array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for _ in range(n):
            nums1.remove(0)

        for i in nums2:
            nums1.append(i)

        nums1.sort()