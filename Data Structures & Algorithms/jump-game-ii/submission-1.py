class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        choose the largest number every time and see where we go from there
        maintain two pointers l, r

        l, r represent the range of reachable indices
        """
        l, r = 0, 0
        steps = 0
        farthest = 0

        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            r = farthest
            steps += 1
        return steps