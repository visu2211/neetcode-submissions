class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, summ, path):
            if i == len(candidates) or summ >= target:
                if summ == target:
                    res.append(path[:])
                return
            
            path.append(candidates[i])
            backtrack(i + 1, summ + candidates[i], path)
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, summ, path)
        
        backtrack(0, 0, [])
        return res