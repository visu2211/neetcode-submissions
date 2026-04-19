class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        countS, countT = defaultdict(int), defaultdict(int)
        for i in t:
            countT[i] += 1
        
        have = 0
        l, r = 0, 0
        size = float("inf")
        res = [-1, -1]
        while r < len(s):
            c = s[r]
            countS[c] += 1
            if c in countT and countS[c] == countT[c]:
                have += 1
            
            while have == len(countT):
                if size > r - l + 1:
                    size = r - l + 1
                    res = [l, r]
                d = s[l]
                countS[d] -= 1
                if d in countT and countS[d] < countT[d]:
                    have -= 1
                l += 1
            r += 1
            
        l, r = res
        return s[l: r + 1] if res != [-1, -1] else ""
                
        #have countT, if have == len(countT): we record a min value

        
        #countT has dictionary 