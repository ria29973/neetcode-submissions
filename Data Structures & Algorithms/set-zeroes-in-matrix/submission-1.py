class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        z_rows = set()
        z_cols = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    z_rows.add(r)
                    z_cols.add(c)
        for r in range(rows):
            for c in range(cols):
                if r in z_rows or c in z_cols:
                    matrix[r][c] = 0
        
        
        