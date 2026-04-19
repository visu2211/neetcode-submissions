class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        res = []

        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
        
        q = deque()

        for crs in range(len(indegree)):
            if indegree[crs] == 0:
                q.append(crs)
        
        while len(q) != 0:
            crs = q.popleft()
            res.append(crs)
            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)

        if len(res) != numCourses:
            return []
        return res[::-1]



