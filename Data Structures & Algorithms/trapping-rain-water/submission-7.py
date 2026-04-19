class Solution:
    def trap(self, height: List[int]) -> int:
        #two pointer with both pointers starting from one place and then traversing forward
        maxLeft = [0] * len(height)
        m = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = m
            m = max(m, height[i])
        
        maxRight = [0] * len(height)
        m = height[-1]
        for i in range(len(height) - 2, -1, - 1):
            maxRight[i] = m
            m = max(m, height[i])
        
        print(maxLeft)
        print(maxRight)
        

        res = 0
        for i in range(len(height)):
            if min(maxLeft[i], maxRight[i]) > height[i]:
                res += min(maxLeft[i], maxRight[i]) - height[i]
        return res       