# symmetric tree
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1,t2):
            if(not t1 and not t2): return True;
            if(not t1 or not t2): return False;
            if(t1.val != t2.val): return False;
            return t1.val == t2.val and isMirror(t1.left,t2.right)and isMirror(t1.right,t2.left)

        return isMirror(root,root)






# 틀린 코드 반례 [1,2,2,2,null,2]
# class Solution:
#
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         global cnt
#         result = []
#         arr = []
#         arr1 = []
#         cnt = 0
#         def dfs(node):
#             global cnt
#             if node is not None:
#                 dfs(node.left)
#                 result.append(node.val)
#                 cnt += 1
#                 dfs(node.right)
#         dfs(root)
#
#         for _ in range((cnt//2)):
#             arr.append(result.pop())
#         for _ in range((cnt//2)):
#             arr1.append(result.pop(0))
#         if arr == arr1:
#             return True
#         return False