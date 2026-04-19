class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        
        def backtrack(i, path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(i + 1, path)
                    path.pop()

        
        backtrack(0, [])
        return res