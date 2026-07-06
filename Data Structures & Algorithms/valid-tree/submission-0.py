class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not (0 <= len(edges) <= (n * (n - 1)) / 2):
            return False

        adjList = defaultdict(list)
        for e, v in edges:
            adjList[e].append(v)
            adjList[v].append(e)
        
        visited = set()

        def dfs(i, parent):
            if i in visited:
                return False
                
            visited.add(i)
            for neigh in adjList[i]:
                if neigh == parent:
                    continue
                elif not dfs(neigh, i):
                        return False                
            return True
        
        return dfs(0, -1) and len(visited) == n

        """
        Inputs / Outputs
            number of nodes
            list of node edges [v1, v2]

            true/false depending on valid tree
        Givens / Assumptions
            0 <= edges.length <= n * (n - 1) / 2

        Example
            Connected - Every node is reachable from every other node (there is exactly one connected component).
                create visited array, if all items are seen then true
            Acyclic - The graph contains no cycles.
                run dfs and keep track of cycle array

            create adj list
            create track array
            run dfs on it
                if cycle return false mid method

            if true return true
        Code
        Edge Cases
        Complexities
        """