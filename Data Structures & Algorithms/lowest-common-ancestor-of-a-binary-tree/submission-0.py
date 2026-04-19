# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #create parent map
        #iterate through ancestors and then switch paths to different one if none so it travels same path

        parent = {root: None}
        def dfs(node):
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        dfs(root)
        
        p1, q1 = p, q
        while p1 != q1:
            p1 = parent[p1] if parent[p1] else q
            q1 = parent[q1] if parent[q1] else p
        return p1