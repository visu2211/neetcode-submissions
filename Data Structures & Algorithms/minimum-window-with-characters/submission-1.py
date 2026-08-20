class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqt = [0] * 58
        freqs = [0] * 58
        se = set(t)
        needed = 0
        for c in t:
            freqt[ord(c) - 65] += 1
            if freqt[ord(c) - 65] == 1:
                needed += 1

        satisfied = 0
        res = [float("-inf"), float("inf")]

        left, right = 0, 0
        while right < len(s):
            freqs[ord(s[right]) - 65] += 1
            if freqs[ord(s[right]) - 65] == freqt[ord(s[right]) - 65]:
                satisfied += 1           
            
            while satisfied == needed:
                if res[1] - res[0] >= right - left:
                    res = [left, right]
                freqs[ord(s[left]) - 65] -= 1
                if freqt[ord(s[left]) - 65] != 0 and freqs[ord(s[left]) - 65] < freqt[ord(s[left]) - 65]:
                    satisfied -= 1
                left += 1
                print(left)
            right += 1

        return "" if res == [float("-inf"), float("inf")] else s[res[0]: res[1] + 1]