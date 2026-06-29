class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Read
            subarray with largest product
        Restate
        Inputs / Outputs
            return largest product
        Givens / Assumptions
            subarray cannot include and negative numbers or else we can just choose empty subarray

            lowest largest possible product = 0
            elements should be contiguous

        Example

            where is the dp here,

            up to this element here is hte largest value

        Code
        Edge Cases
        Complexities

        didnt account for multiple negatives in a row
        """
        #up till i, that is the largest product
        largestProduct = max(nums)
        maxi = mini = 1
        for n in nums:
            if n == 0:
                maxi = mini = 1
                continue
            tmp = maxi * n
            maxi = max(n * maxi, n * mini, n)
            mini = min(tmp, n * mini, n)
            largestProduct = max(largestProduct, maxi, mini)
        return largestProduct

            
