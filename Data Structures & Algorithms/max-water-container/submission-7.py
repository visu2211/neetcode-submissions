class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        we want to maximize area
            need a max variable to hold final value
        
        bounded by the minimum height

        area = (r - l + 1) * min(heights[r], heights[l])
        """
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
