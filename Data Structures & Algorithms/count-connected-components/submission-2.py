class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        iterate from 0 - n
            dfs for each one
        keep track of a visited
        if node in seen then continue else increment number of total components

        if you're in a cycle get out
            
        """
        res = 0
        visited = set()
        adjList = defaultdict(list)

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(i, parent):
            visited.add(i)
            
            for neigh in adjList[i]:
                if neigh not in visited:
                    dfs(neigh, i)
                
                if neigh == parent:
                    continue
            return
                

            
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)
        return res
