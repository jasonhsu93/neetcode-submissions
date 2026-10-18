class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # rotate left by 90 degrees
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # flip each row 
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[i])-1-j]
                matrix[i][len(matrix[i])-1-j] = temp