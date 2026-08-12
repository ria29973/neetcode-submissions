class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()
        def dfs(r, c, ocean):
            for dx, dy in dirs:
                new_r = r + dx
                new_c = c + dy
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if heights[new_r][new_c] >= heights[r][c]:
                    if (new_r, new_c) not in ocean:
                        ocean.add((new_r, new_c))
                        dfs(new_r, new_c, ocean)
        for c in range(cols):
            pac.add((0, c))
            dfs(0, c, pac)
            atl.add((rows - 1, c))
            dfs(rows-1, c, atl)
        for r in range(rows):
            pac.add((r, 0))
            dfs(r, 0, pac)
            atl.add((r, cols-1))
            dfs(r, cols-1, atl)
        res = []
        for arr in pac:
            if arr in atl:
                res.append(list(arr))
        return res


            
        
        