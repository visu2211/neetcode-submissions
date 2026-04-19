class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, summ, path):
            if i == len(nums) or summ >= target:
                if summ == target:
                    res.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(i, summ + nums[i], path)
            path.pop()
            backtrack(i + 1, summ, path)

        backtrack(0, 0, [])
        return res