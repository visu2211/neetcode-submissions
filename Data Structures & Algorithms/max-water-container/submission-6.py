class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #find the current area and set it to the max
        #two pointer
        #if left height is greater than right height move the right height

        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res