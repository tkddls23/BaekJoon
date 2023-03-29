# Convert Sorted Array to Binary Search Tree
# 이진 트리 변환
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            print(root)
            root.left = tree(left, mid - 1)
            root.right = tree(mid + 1, right)
            return root

        return tree(0, len(nums) - 1)
