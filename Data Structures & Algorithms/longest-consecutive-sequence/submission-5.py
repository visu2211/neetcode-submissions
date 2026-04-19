class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in s:
            length = 0
            if n - 1 not in s:
                length = 1
            while (n + length) in s:
                length += 1
            longest = max(longest, length)
        return longest