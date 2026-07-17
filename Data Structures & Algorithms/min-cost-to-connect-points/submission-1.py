class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        PRIMS algorithm
            pop the smallest edge weight
            if node is already seen skip it
            add all the edges to the queue

            (there will be a lot of skipping)



        brute force:
            create an adjacency list where each point is connected to one another

            for each point
                find the closest point
                add the cost to it
                for the neighbor, remove the current point from the all (cant have duplicate edges)

            walkthrough:
                [[0,0],[2,2],[3,3],[2,4],[4,2]]
                mC = 0 + 4 + 2

                0: (2, 2), (3, 3), (2, 4), (4, 2)
                1: (3, 3), (2, 4), (4, 2)
                2: (2, 4), (4, 2)
                3: (4, 2)
                4: (2, 2), (2, 4)
        
        efficient:
            BFS
            visited
            mC = 0
            add each root to the queue
        """
        adjList = defaultdict(list)
        minCost = 0
        for i in range(len(points)):
            x, y = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                nx, ny = points[j]
                dist = abs(x - nx) + abs(y - ny)
                adjList[i].append((dist, j))
        
        queue = []
        visited = set()
        queue.append((0, 0))
        while len(visited) < len(points):
            cost, ind = heapq.heappop(queue)
            if ind in visited:
                continue
            
            visited.add(ind)
            minCost += cost
            for neigh in adjList[ind]:
                heapq.heappush(queue, neigh)
        return minCost


        
        
