class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True
            
            visited.add(node)
            for neigh in adjList[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    #cycleStart is the end of the cycle
                    #we have this line which checks if we found the start
                    #once we find the start, we change to -1 to end it
                    if node == cycleStart:
                        cycleStart = -1
                    #some nodes are not included in the cycle
                    #by setting cycleStart to -1, we effectively stop adding other nodes
                    return True
            return False

        dfs(1, -1)

        for a, b in edges[::-1]:
            if a in cycle and b in cycle:
                return [a, b]

        """
        1 -> 2, 3
        2 -> 

        we build the graph, as soon as we notice a cycle, we know 
        """



        """
        input / output
            list of edges with a redundant edge
            return edge that can be removed to make graph connected / non-cyclical
        givens / assumptions
        constraints
            no repeated edges
            no self loops in the input

        examples
            add each edge and check if there is a cycle
            if there is one when you add an edge, then you know that this is a redundant one

            that would work if it was first edge

            there is only one redundant edge.
            that can yeild multiple possible answers

            create the graph
            moving backwards exclude the edge and see if its still a cycle. if it is move on

            create adjacency list
            iterating edges from the end. remove the pairing
            run hasCycle, if true found else keep iterating forward
        code
        edge cases
        complexities
        """
