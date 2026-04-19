class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for index, value in enumerate(nums):
            if target - value in hMap:
                return [hMap[target - value], index]
            hMap[value] = index
        return