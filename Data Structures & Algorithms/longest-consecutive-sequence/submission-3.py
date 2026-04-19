class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums))
        nums.sort()
        print(nums)
        maxSeq = 1
        seq = 1
        for index in range(len(nums) - 1):
            if nums[index] + 1 == nums[index + 1]:
                seq += 1
                if maxSeq < seq:
                    maxSeq = seq
            else:
                seq = 1
        return maxSeq
        