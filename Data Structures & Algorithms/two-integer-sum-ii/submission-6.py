class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hMap = {}
        for i, v in enumerate(numbers):
            if target - v in hMap:
                return [hMap[target - v], i + 1]
            hMap[v] = i + 1