# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        
        def dfs(node):

            if not node:
                return False

            if node.val == subRoot.val:
                if same(node, subRoot):
                    return True

            return dfs(node.right) or dfs(node.left)

        def same(node1, node2):

            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            left = same(node1.left,node2.left)
            right = same(node1.right,node2.right)

            return left and right 

        return dfs(root)
            

            