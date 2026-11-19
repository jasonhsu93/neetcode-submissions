class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def bfs(x, y):
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            queue = deque()
            seen = set()
            seen.add((x,y))
            queue.append([x, y, 0, seen])

            while len(queue) > 0:
                temp = queue.popleft()
                tempWord = board[temp[1]][temp[0]]
                tempSeen = temp[3]
                if tempWord == word[temp[2]] and temp[2] == len(word) - 1:
                    return True
                if tempWord == word[temp[2]]:
                    x = temp[0] 
                    y = temp[1]
                    i = temp[2] + 1 
                    for direction in directions:
                        if x + direction[0] >= 0 and x + direction[0] < len(board[0]) and y + direction[1] >= 0 and y + direction[1] < len(board)\
                        and board[y + direction[1]][x + direction[0]] == word[i]:
                            if (x + direction[0],y + direction[1]) not in tempSeen:
                                next_seen = tempSeen | {(x + direction[0],y + direction[1])}
                                queue.append([x + direction[0],y + direction[1], i, next_seen])

            return False
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    if bfs(x,y):
                        return True

        return False