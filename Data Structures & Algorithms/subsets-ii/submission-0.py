class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        """
        Read
        Restate
        I/O
        Assumptions
        Example
        Code
        Edge Cases
        Complexities

        problem
        subsets of different orders are stored even when their contents are duplicates

        """

        res = []
        nums.sort()
        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return res