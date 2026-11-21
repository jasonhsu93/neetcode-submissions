class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        seen = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(i, seen, coordinate):
            x = coordinate[0]
            y = coordinate[1]

            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board): 
                return False
            if tuple(coordinate) not in seen and board[y][x] == word[i] and i == len(word) - 1:
                return True
            if tuple(coordinate) in seen or board[y][x] != word[i] or i >= len(word):
                return False

            seen.add(tuple(coordinate))
            exist = False

            for direction in directions:
                newX = coordinate[0] + direction[0]
                newY = coordinate[1] + direction[1]
                exist = dfs(i + 1, seen.copy(), [newX,newY])
                if exist:
                    break

            return exist

        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs(0, seen.copy(), [x,y]):
                    return True

        return False