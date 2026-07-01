class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        find cells where water flows from that cell to both the pacific and atlantic

        what are the conditions where the water can take both

        Idea:
            Keep a set of coordinates for pacific and a separate one for atlantic
            add borders into res
            For every cell, check if water can flow into both oceans, use dfs

        Problem:
            How do we know if it reached both
            If a cell can flow into water, and we know that we have a possbile neighboring cell that can we can downflow to, we also know that cell can go into water
        """
        atlantic = set()
        pacific = set()
        r, c = len(heights), len(heights[0])

        def dfs(i, j, visit, prevHeight):
            if (i, j) in visit or not(0 <= i < r) or not(0 <= j < c) or prevHeight > heights[i][j]:
                return

            visit.add((i, j))
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])


        for i in range(r):
            dfs(i, 0, pacific, 0)
            dfs(i, c - 1, atlantic, 0)
        
        for j in range(c):
            dfs(0, j, pacific, 0)
            dfs(r - 1, j, atlantic, 0)
        
        return list(atlantic & pacific)      