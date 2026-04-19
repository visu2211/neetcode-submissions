class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        maxLength = 0
        seen = set()

        l, r = 0, 0
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            maxLength = max(r - l + 1, maxLength)
            r += 1
        return maxLength