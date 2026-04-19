# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            subList = []
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                subList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(subList)
        return res

        """
          We have an integer array “views” of length n, where “views[i]” represents
           the total number of views for a new Netflix series on day i after launch. Given a start date input and an end date input
           return the size of the largest jump in view numbers within these dates.

           inputs: 
           - views - array where views[i] represents number of views
           - start date - int
           - end date - int

           output:
           - size of largest jump

           constraints:
           - start <= i < = end

           [5, 6, s8, 4, 7, 2, 9, e3, 1] -> 7
           [5, 6, s10, 4, 7, 9, e3, 1] -> 7
        """

        #shrink window to start, end date
        #find max, min in window
        #return max - min

# class Solution:
#     def largestJumpinViews(self, views: List[int], startDate: int, endDate: int) -> int:
#         res = 0
#         for i in range(startDate, endDate) :
#             res = max(abs(views[i + 1] - views[i]), res)
#         return res

        
        