# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if p == q:
            return p
        
        lp = []
        lq = []

        def findTarget(root, l, target):
            if root.val > target.val:
                l.append(root)
                findTarget(root.left, l, target)
            elif root.val < target.val:
                l.append(root)
                findTarget(root.right, l, target)
            else:
                l.append(target)
        findTarget(root, lp, p)
        findTarget(root, lq, q)

        #both arrays now loaded with ancestors
        sp = set(node.val for node in lp)
        sq = set(node.val for node in lq)
        common_vals = sp & sq
        for node in reversed(lp):
            if node.val in common_vals:
                return node