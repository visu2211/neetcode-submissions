class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return res