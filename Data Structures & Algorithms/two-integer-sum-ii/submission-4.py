class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num], index + 1]
            dic[num] = index + 1