class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Inputs / Outputs
            an array of nums
            lists of distinct indices where corresponding values sum to zero
        Assumptions
            array is not sorted
        Example

        Code
        Edge Cases
        Complexities
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif summ < 0:
                    l += 1
                else:
                    r -= 1
        return res