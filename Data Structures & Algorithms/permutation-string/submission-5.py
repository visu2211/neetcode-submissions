class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window
        if len(s1) > len(s2):
            return False
        #hMap for s1
        c1 = defaultdict(int)
        for s in s1:
            c1[s] += 1

        c2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            c2[s2[r]] += 1
            if r - l + 1 < len(s1):
                continue
            if c1 == c2:
                return True
            c2[s2[l]] -= 1
            if c2[s2[l]] == 0:
                del c2[s2[l]]
            l += 1
            r += 1
        return False