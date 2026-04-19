class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshOranges = 0
        minutes = 0
        directions = ([1, 0], [-1, 0], [0, 1], [0, -1])
        rows, cols = len(grid), len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshOranges += 1
                if grid[i][j] == 2:
                    q.append([i, j])


        while freshOranges and q:
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                for dx, dy in directions:
                    if not(0 <= x + dx < rows and 0 <= y + dy < cols) or grid[x + dx][y + dy] == 2:
                        continue
                    if grid[x + dx][y + dy] == 0:
                        continue
                    if grid[x + dx][y + dy] == 1:
                        freshOranges -= 1
                        grid[x + dx][y + dy] = 2
                        q.append([x + dx, y + dy])
            minutes += 1
        
        return -1 if freshOranges else minutes
            