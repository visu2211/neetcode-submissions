class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        copy = nums.copy()
        if 0 in copy:
            i = nums.index(0)
            copy.pop(i)
            if (0 in copy):
                return [0 for i in range(len(nums))]
        product = 1
        for i in copy:
            product *= i
        for num in range(len(nums)):
            if nums[num] == 0:
                nums[num] = product
            else:
                if len(copy) < len(nums):
                    nums[num] = 0
                else:
                    nums[num] = int(product / nums[num])
        return nums