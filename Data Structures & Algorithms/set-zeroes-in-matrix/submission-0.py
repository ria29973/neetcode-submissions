class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros.add((r, c))
        for r, c in zeros:
            for cur_r in range(rows):
                matrix[cur_r][c] = 0
            for cur_c in range(cols):
                matrix[r][cur_c] = 0
        
        
        