class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []

        if len(nums) < 3:
            return []

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                print(i, l, r)
                if nums[i] + nums[l] + nums[r] == 0:
                    if (nums[i], nums[l], nums[r]) not in seen:
                        res.append([nums[i], nums[l], nums[r]])
                        seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
        return res