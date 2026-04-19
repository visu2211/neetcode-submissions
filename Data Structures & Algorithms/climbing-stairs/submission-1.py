class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Read
        Restate
        I/O
            number of steps to reach to the top of the staircase
            number of distinct ways to climb to the top
        Assumptions
            O(N) time and space
        Example
        Code
        Edge Cases
        Complexities

        1 2 3 4 
        1 2 3 5

        from n - 2, we take two steps which makes
        so 
        1 + 1 + 2 to get to 4
        2 + 2 to get to 4
        we already have 2 ways to get there, so by adding 2 steps we are not increasing the amount of ways

        n - 1
        1 + 2
        
        2 + 1
        1 + 1 + 1

        Sub problem is n = [n - 1] + [n - 2]

        """
        if n < 3:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]