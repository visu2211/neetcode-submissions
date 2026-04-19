class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Linear Time Solution
        #Two Pointer Technique
        left, right = 0, len(heights) - 1
        maxArea = area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxArea

        #BRUTE FORCE
        maxArea, area = 0, 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])
                area = width * height
                maxArea = max(maxArea, area)
        return maxArea