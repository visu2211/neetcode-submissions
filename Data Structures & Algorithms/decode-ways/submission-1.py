class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(i):

            #means youve reached the end, a leaf
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            if i in cache:
                return cache[i]

            #regardless we can always count as a single letter so always propel dfs unless 0
            ways = dfs(i + 1)

            #if in bounds and two integers < 26, we can also run dfs on a path including that except skipping two letters.
            if i + 1 <= len(s) - 1 and int(s[i: i + 2]) <= 26:
                ways += dfs(i + 2)
            cache[i] = ways
            return ways
        return dfs(0)

            

        """
        decision tree
        we move forward from the first integer
        we check if integer is valid (not zero)
            we also check if two integers together is valid < 26

            if that is the case we 1 + dfs and keep moving forward
        """

        """
        Read
        Restate
        Givens / Assumptions
            01 is invalid cannot have leading 0s
            answer fits in a 32 bit integer
        Inputs / Outputs
            s containing only digits

            number of ways to decode it
        Example

            1 0 2 3

            10 2
            10 23

            1 2 2 1
            1 2 2 1
            12 2 1
            12 21
            1 22 1
            1 2 21

            two pointers

            one starts at the first index and moves forward when value is greater than 26
            second starts just right of the first index and moves to the end


            0 1
            if zero is ever the first digit in a subgroup, we must skip
            if zero is ever alone we must skip it

            we try all possible combinations of values, if they are valid we increment

            if left pointer is a zero, we can skip it since we know all combinations will be invalid
        Code
        Edge Cases
        Complexities
        """