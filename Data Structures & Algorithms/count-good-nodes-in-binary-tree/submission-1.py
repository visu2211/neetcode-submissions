# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count = 0

        #how to check if values greater, keep track of the max in the current path, if val is greater then it is a good node

        def dfs(node, maxi):
            if node.val >= maxi:
                self.count += 1
                maxi = node.val
            
            if node.left:
                dfs(node.left, maxi)
            
            if node.right:
                dfs(node.right, maxi)
        
        dfs(root, float("-inf"))
                

        return self.count