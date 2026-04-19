class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        """
        inputs - cost to take a step from that floor
        output - final minimum cost to reach top floor

        sub problem - cost to get to current step

        #bottom up dp (tabulation)

        """
        dp = [0] * (len(cost) + 1)
        dp[1], dp[2] = 0, 0


        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[-1]
            

