class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for pre, crs in prerequisites:
            prereqs[pre].append(crs)
        
        state = [0] * numCourses
        def dfs(crs):
            if state[crs] == 1:
                return False
            
            if state[crs] == 2:
                return True
            
            state[crs] = 1
            for neigh in prereqs[crs]:
                if not dfs(neigh):
                    return False
            state[crs] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
