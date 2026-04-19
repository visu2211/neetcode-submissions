class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqList = defaultdict(int)
        maxi = 0
        maxf = 0
        l = 0
        for r in range(len(s)):
            freqList[s[r]] += 1
            if maxf < freqList[s[r]]:
                maxf = freqList[s[r]]
            if r - l + 1 - maxf > k:
                freqList[s[l]] -= 1
                l += 1
            if maxi < r - l + 1:
                maxi = r - l + 1
        return maxi