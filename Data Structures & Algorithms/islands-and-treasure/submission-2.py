class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        """
        fill each land cell with the distance to its neartest treasure chest
        if land cell cannot be traversed, value should remain inf

        traverse cardinal directions

        shortest distance to treasure chest from land cell
            BFS

        [l,-1,0,l],
        [l,l,l,-1],
        [l,-1,l,-1],
        [0,-1,l,l]

        distance = 0
        0, 2
        3, 0
        process these coordinates and increment the distance


        [3,-1,0,1],
        [2,2,1,-1],
        [1,-1,2,-1],
        [0,-1,3,4]

        we can start from land cell, traverse through till we find a chest
        we can start from the treasure chests and spread outwards from there
            if the land cell has not been visited we add to queue
            if it has we know it has the smallest value it can since it was reached already


        at every land cell that is inf we perform bfs to find closest treasure chest
        grid[i][j] = dfs()

        """
        queue = deque([])
        r, c = len(grid), len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    queue.append((i, j))

        #all treasure chest locations are in the queue
        distance = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                grid[x][y] = distance
                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = dx + x, dy + y
                    if not(0 <= nx < r and 0 <= ny < c) or grid[nx][ny] != INF:
                        continue
                    
                    #cell is in bounds, a land cell, and an unseen land cell
                    grid[nx][ny] = -1
                    queue.append((nx, ny))
            distance += 1