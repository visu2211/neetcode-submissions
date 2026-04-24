# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #either include it in the diamter or contribute it to something higher

        res = 0

        def diameter(node):
            if node is None:
                return 0

            l = diameter(node.left)
            r = diameter(node.right)

            nonlocal res
            res = max(res, l + r)
            return 1 + max(l, r)

        diameter(root)
        return res