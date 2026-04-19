class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hMap = defaultdict(int)
        arr = sorted(heights)
        for i in arr:
            height = 0
            curr = 0
            for j in range(len(heights)):
                if heights[j] >= i:
                    curr += i
                    if curr > height:
                        height = curr
                else:
                    curr = 0
            hMap[i] = height
        return max(hMap.values())