class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(y,x):
            queue = deque()
            queue.append([y,x])
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            while len(queue) > 0:
                temp = queue.popleft()
                y = temp[0]
                x = temp[1]

                for direction in directions:
                    tempY = y + direction[0]
                    tempX = x + direction[1]
                    if tempY >= 0 and tempY < len(grid) and tempX >= 0 and tempX < len(grid[0]) and grid[tempY][tempX] == '1':
                        grid[tempY][tempX] = '!'
                        queue.append([tempY,tempX]) 

 
        count = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    bfs(y,x) 
                    count += 1
                else:
                    grid[y][x] = '!'

        return count
        

        
