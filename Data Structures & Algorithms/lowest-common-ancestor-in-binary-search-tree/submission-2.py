# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ptr = root
        d = deque([[root, None]])
        parentMap = {}

        while d:
            child, parent = d.popleft()
            parentMap[child] = parent

            if child.left:
                d.append([child.left, child])

            if child.right:
                d.append([child.right, child])
        
        p1, q1, = p, q

        while p1 != q1:
            p1 = parentMap[p1]
            if p1 == None:
                p1 = q

            q1 = parentMap[q1]
            if q1 == None:
                q1 = p

        return p1
            
            