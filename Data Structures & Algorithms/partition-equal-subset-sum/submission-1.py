class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """
        Read
            sum(subset1) == sum(subset2)
        Restate
        Inputs / Outputs
            array of positive integers

            true / false whether partition of equal sum can be created
        Givens / Assumptions
            all numbers are positive
            all numbers should be covered once across both subsets (Mutually Exclusive, Collectively Exhaustive)

            DP problem
        Example
            [1, 2, 3, 4] --> [1, 4], [2, 3]

            how can we separate this into smaller parts

            we dont need to keep track of the subsets, just need to return true / false

            O(n * t) --> iterate through each element in the set and then for each element check all the items in subset

            1 234
            12 34
            123 4
            13 24
            14 23
        Code
        Edge Cases
        Complexities
        """
        #cannot be split into perfect half
        summ = sum(nums)
        if summ % 2 == 1:
            return False
        
        half = summ / 2
        #if we find a subset that sums to half of the total sum then we know the remaining half should also add up
        #now we need to find a subset that has sums to half
        cache = set([0])
        for n in nums[::-1]:
            for x in list(cache):
                if x + n not in cache:
                    cache.add(x + n)
            if half in cache:
                return True
        return False
        """
        1, 2, 3, 4
        0, 1, 2, 3

        0, 0
            1, 1
                2, 3
                    3, 6
                        4, 10
                        4, 6
                    3, 3
                        4, 7
                        4, 3
                2, 1
                    3, 4
                        4, 8
                        4, 4
                    3, 1
                        4, 5
                        4, 1
            1, 0
                2, 2
                    3, 5
                        4, 9
                        4, 5
                    3, 2
                        4, 6
                        4, 2
                2, 0
        """

