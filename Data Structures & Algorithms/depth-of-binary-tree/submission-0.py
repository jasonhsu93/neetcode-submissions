# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def dfs(node, depth):
            
            if node == None:
                return depth

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            return max(left if left else 0,right if right else 0)

        return dfs(root, 0)