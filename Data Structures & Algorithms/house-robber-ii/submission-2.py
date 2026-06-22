class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        def dfs(i, arr, cache):
            if i >= len(arr):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(dfs(i + 1, arr, cache), arr[i] + dfs(i + 2, arr, cache))
            return cache[i]
        
        return max(dfs(0, nums[1:], {}), dfs(0, nums[:-1], {}))
        """
        Read
        Restate
        Inputs / Outputs
            nums = reprents amount of money ith house has

            return max amount you can rob without getting caught
        Givens / Assumptions
            hours are arranged in a circle --> first and last hourses are neighbors
        Example
            this is house robber 1 except now we have to consider neighboring houses at the end

            2 9 8 3 6
            2 9 10 12 15

            how can we have memory that we used the first one so we cant use the last one

            our cache represents the max amount of money we can rob at that index.
            for each call that used the first we want to make sure that we cant use the last

            dfs(i)

            first = 0


            through recursive calls I want to know if we used the first one or not
            we can have a variable that tracks that

        Code
        Complexities

        make a ciruclar structure, once cycle detected we stop
        """