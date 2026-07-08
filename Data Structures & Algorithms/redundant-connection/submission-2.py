class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        #this is a cyclic graph
        for a, b in edges[::-1]:
            adjList[a].remove(b)
            adjList[b].remove(a)
            #check if cycle does not exist, we found redundant edge
            if not(self.hasCycle(a, -1, adjList, set())) and not(self.hasCycle(b, -1, adjList, set())):
                return [a, b]
            #if it still exists, add back and iterate backwards
            adjList[a].append(b)
            adjList[b].append(a)

    def hasCycle(self, node, parent, adjList, visited):
        if node in visited:
            return True

        visited.add(node)
        for neigh in adjList[node]:
            if neigh == parent:
                continue
            elif self.hasCycle(neigh, node, adjList, visited):
                return True
        return False

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
