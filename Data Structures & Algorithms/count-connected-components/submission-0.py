class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        for i in range(n):
            if i not in visited:
                components += 1
                self.dfs(i, adjList, visited)

        return components

    def dfs(self, i, adjList, visited):
        visited.add(i)
        for neigh in adjList[i]:
            #avoids infinite loop
            if neigh not in visited:
                self.dfs(neigh, adjList, visited)
        """
        inputs / outputs
            given a graph of nodes

            return number of components
        constraints
            no repeated edges
        givens / assumptions
            edges between two vertices
        example
            n = 5, edges = [[0,1],[1,2],[3,4]]

            we can run dfs on every node and add it to visited. everytime we encounter a new node we increment

            numofcomp = 0
            create adj list
            for 0 - n
                everytime a node is not in the list we add one and call dfs on it
                numofcomp += 1
                dfs(i)
                    add to visited
                    spread forward

            return numofocomp
        code
        edge cases
        complexities
        """