class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Inputs / Outputs
        Givens / Assumptions
        Constraints
        Example
        Code
        Edge Cases
        Complexities

        djikstras algorithm
            dfs, but at each possible route take the smallest weight

        k = root
        visited
        dfs
            add root to visited
        """
        totalTime = 0
        adjList = defaultdict(list)

        #builds adjacency list
        #makes it so that shortest travel time is first entry in list
        # Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
        # need to deduct time as we spread, if two neighbors have the same time we execute them both
        """
        times=[[1,2,1],[2,3,7],[1,3,4],[2,1,2]] n=4 k=1
        1: [(2, 1), (3, 4)]
        2: [(3, 7), (1, 2)]

        totalTime = 4
        visited = (1, 2, 3, 4)
        queue = [(4, 4)]        
        """
        for u, v, t in times:
            adjList[u].append((v, t))
        
        if k not in adjList:
            return -1

        visited = set()
        queue = [(0, k)]
        while queue and len(visited) != n:
            time, node = heapq.heappop(queue)
            if node in visited:
                continue
            
            totalTime = time
            visited.add(node)
            for neigh, time in adjList[node]:
                if neigh not in visited:
                    heapq.heappush(queue, (totalTime + time, neigh))
        return -1 if len(visited) != n else totalTime
