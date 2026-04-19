class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep track of minPrice
        #keep track of maxProfit

        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPrice)
            minPrice = min(prices[i], minPrice)
        return maxProfit
