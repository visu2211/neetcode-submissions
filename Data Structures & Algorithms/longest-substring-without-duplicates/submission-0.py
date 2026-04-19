class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxi = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            if maxi < len(charSet):
                maxi = len(charSet)
        return maxi