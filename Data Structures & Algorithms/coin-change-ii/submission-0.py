class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        number of distinct combinations to make up an amount
        each coin value is unique
        unlimited number of each coin

        recursive question, either add current coin or skip and go to next
        this is 2^n not efficient

        Optimal Solution

        how can we convert to 2d array

        what is the repeating factor (recurrence relation)

            the intermediary build up is making 1, 2, 3... dollars till we get to amount
            for coin change 1 we wanted to see if it was possible
            now we want to track the number of distinct ways to get to that combination

            1, 2, 3 | a = 4

            inf inf inf inf
            fi
        
        """
        coins.sort()
        n = len(coins)

        dp = [[0 if i != 0 else 1 for i in range(amount + 1)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            coin = coins[i]
            for a in range(1, amount + 1):
                if a >= coin:
                    dp[i][a] = dp[i + 1][a] + dp[i][a - coin]
        
        return dp[0][amount]

            
        