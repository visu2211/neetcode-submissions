class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        start from the end and see if we can reach the end from the previous ones
        want to shift the end (last index) as close to the beginning
        """

        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0