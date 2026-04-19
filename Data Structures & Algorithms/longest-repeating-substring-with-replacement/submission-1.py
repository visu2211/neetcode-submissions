class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        #keep track of the most frequent occuring character
        #as long as up to k characters keep increasing window
        #if k is exceeded start decreasing the window

        #how to update maxFreq when decreasing

        l, r = 0, 0
        
        freqList = defaultdict(int)
        maxFreq = 0
        res = 0

        while r < len(s):
            freqList[s[r]] += 1
            maxFreq = max(maxFreq, freqList[s[r]])
            while l <= r and (r - l + 1) - maxFreq > k:
                freqList[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res