# maximum depth of binary tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def deep(node,depth):
            result = depth
            if node is None:
                return 0
            if node.left is not None:
                result = deep(node.left,depth+1)
            if node.right is not None:
                result = max(result,deep(node.right,depth+1))
            return result


        return deep(root,1)