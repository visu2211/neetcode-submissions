class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        for s in strs:
            so = ''.join(sorted(s))
            if so in hMap:
                hMap[so].append(s)
            else:
                hMap[so] = [s]
        return list(hMap.values())