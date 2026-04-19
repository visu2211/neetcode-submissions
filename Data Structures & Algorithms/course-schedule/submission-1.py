class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(set)
        for crs, pre in prerequisites:
            prereqs[crs].add(pre)
        
        visited = [0] * numCourses
        
        def dfs(i):
            if i == numCourses:
                return True
            
            if visited[i] == 2:
                return True
            
            if visited[i] == 1:
                return False
            
            visited[i] = 1
            for pres in prereqs[i]:
                if not dfs(pres):
                    return False
            visited[i] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True