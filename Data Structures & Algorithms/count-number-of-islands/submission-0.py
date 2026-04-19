class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        islands = 0
        
        def dfs(i, j):
            if not(0 <= i < len(grid)) or not(0 <= j < len(grid[0])):
                return
            
            if grid[i][j] == "1":
                grid[i][j] = "X"

                for x, y in directions:
                    dfs(i + x, j + y)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands