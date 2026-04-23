class Solution:
    def trap(self, height: List[int]) -> int:
        
        """"
        Inputs / Outputs
            array of heights
            max water that can be trapped
        Assumptions
            no water can be trapped on the ends 
        Example
            two pointer problem
            water is bound by the min(tallest bar to the left, tallest bar to the right)

            min(leftMax, rightMax) - heights[i]

        Edge Cases
        Code
        Complexities
        """
        #store the bars to the tallest bar to the left and right with prefix arrays
        n = len(height)
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])

        totalWater = 0
        for i in range(n):
            totalWater += max(0, min(left[i], right[i]) - height[i])
        return totalWater