class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i, v in enumerate(nums):
            if target - v in hMap:
                return [hMap[target - v], i]
            hMap[v] = i
