class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)

        for crs, pre in prerequisites:
            prereqs[crs].append(pre)
        
        state = [0] * numCourses

        #houses paths in order from no prereq class to all prereq class
        path = []

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
            #classes with no prereqs are processed first since the dfs goes all the way to the highest class
            path.append(crs)
            #works out well with the problem
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return path