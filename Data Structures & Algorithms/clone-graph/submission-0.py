"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        start = Node(node.val,[])
        queue = deque() 
        queue.append([node,start])
        created = {}
        created[node.val] = start 

        while len(queue) > 0:
            temp = queue.popleft()
            original_node = temp[0]
            clone_node = temp[1] 
            for neighbor in original_node.neighbors:
                if neighbor.val in created:
                    clone_node.neighbors.append(created[neighbor.val])
                else:
                    new_node = Node(neighbor.val, [])
                    clone_node.neighbors.append(new_node)
                    created[neighbor.val] = new_node
                    queue.append([neighbor,new_node])

        return start 