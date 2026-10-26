# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        cache = []
        cache.append(root)
        res = []

        while len(cache) > 0:
            temp = []
            new = []
            for node in cache:
                temp.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            
            cache = new
            res.append(temp)

        return res