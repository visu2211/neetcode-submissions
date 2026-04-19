class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #BFS Solution

        maxArea = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(x, y):
            area = 1
            q = deque()
            q.append((x, y))
            grid[x][y] = 0

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == 1:
                        q.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = 0
                        area += 1

            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i, j))
        
        return maxArea

        """
        How to load all the starting roots into the queue
        you cant differentiate between land part of the same islands

        You can also create a method for bfs

        """