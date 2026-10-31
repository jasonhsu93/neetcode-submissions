# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         
        def dfs(node, prev):

            if not prev[0]:
                return [False, prev[1]]

            if node.left:
                prev = dfs(node.left, prev) 

            if node.val <= prev[1]: 
                return [False, prev[1]]
            else:
                prev[1] = node.val

            if node.right:
                prev = dfs(node.right, prev)

            return prev

        return dfs(root, [True, -float('inf')])[0]