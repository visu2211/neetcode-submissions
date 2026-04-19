"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        hMap = {}
        def dfs(node):
            if node.val not in hMap:
                hMap[node.val] = Node(node.val)
            for n in node.neighbors:
                if n.val not in hMap:
                    dfs(n)
            
            for neigh in node.neighbors:
                hMap[node.val].neighbors.append(hMap[neigh.val])
        dfs(node)
        return hMap[node.val]
        """
        Givens
            connected undirected graph
            return a deep copy of new nodes of the graph

            node has val and neighbor attributes

        Example

        Edge Cases

        Code

        Complexities


        """