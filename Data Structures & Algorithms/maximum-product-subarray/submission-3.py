class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #we want to keep track of a max and min since negative numbers are involved
        largestProduct = max(nums)
        maxi = mini = 1
        for n in nums:
            #we reset when we encounter a 0 cuz all of the preceding values will turn to 0
            if n == 0:
                maxi = mini = 1
                continue
            
            #max of cur value, cur value * something, or cur value times negative
            tmp = n * maxi
            maxi = max(n * maxi, n, n * mini)
            mini = min(tmp, n, n * mini)
            largestProduct = max(largestProduct, maxi, mini)
        return largestProduct