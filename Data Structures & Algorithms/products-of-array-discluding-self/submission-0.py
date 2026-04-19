class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        copy = nums.copy()
        if 0 in nums:
            i = nums.index(0)
            copy.pop(i)
            if 0 in copy:
                return [0 for i in range(len(nums))]
        product = 1
        for num in copy:
            product *= num
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = int(product)
            else:
                if len(copy) < len(nums):
                    nums[i] = 0
                else:
                    nums[i] = int(product / nums[i])
        return nums
