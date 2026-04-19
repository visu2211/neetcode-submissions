"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #want to make a method that returns values from dfs so you dont iterate neighbors twice
        #node to new node
        hMap = {}

        def dfs(node):
            if node in hMap:
                return hMap[node]
            
            new = Node(node.val)
            hMap[node] = new

            for neigh in node.neighbors:
                new.neighbors.append(dfs(neigh))

            return new
        return dfs(node) if node else None
