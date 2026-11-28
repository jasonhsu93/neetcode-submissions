class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def bfs(r,c):

            queue = deque()
            queue.append([r,c])
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            pacific = False
            atlantic = False
            seen = set()

            while len(queue) > 0:
                temp = queue.popleft()

                if temp[1] <= 0 and temp[0] >= len(heights) - 1: 
                    pacific = True
                    atlantic = True
                elif temp[1] >= len(heights[0]) - 1 and temp[0] <= 0: 
                    pacific = True
                    atlantic = True
                elif temp[0] <= 0 or temp[1] <= 0:
                    pacific = True
                elif temp[0] >= len(heights) - 1 or temp[1] >= len(heights[0]) - 1:
                    atlantic = True

                if pacific and atlantic:
                    return True
 
                for direction in directions:
                    new_r = temp[0] + direction[0]
                    new_c = temp[1] + direction[1]

                    if new_r >= 0 and new_c >= 0 and new_r < len(heights) and new_c < len(heights[0]) and heights[new_r][new_c] <= heights[temp[0]][temp[1]] and (new_r,new_c) not in seen:
                        if both[new_r][new_c] and heights[new_r][new_c] <= heights[temp[0]][temp[1]]:
                            return True
                        queue.append([new_r, new_c]) 
                        seen.add((new_r,new_c))

            return False

        res = []
        both = [[False] * len(heights[0]) for _ in range(len(heights))]

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if both[r][c] or bfs(r,c):
                    res.append([r,c])
                    both[r][c] = True

        return res

