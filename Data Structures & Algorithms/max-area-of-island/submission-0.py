class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #DFS Solution

        maxArea = 0

        def dfs(x, y):
            if not(0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1):
                return 0
            
            grid[x][y] = 0
            return dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1) + 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(maxArea, dfs(i, j))
        
        return maxArea