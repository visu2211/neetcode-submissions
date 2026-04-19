class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finList = []
        anaDict = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in anaDict.keys():
                anaDict[key].append(s)
            else:
                anaDict[key] = [s]
        return list(anaDict.values())