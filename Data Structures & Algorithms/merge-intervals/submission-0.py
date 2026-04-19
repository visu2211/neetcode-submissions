class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        intervals.sort()
        
        merged = []
        merged.append(intervals[0])

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if merged[-1][1] >= s and merged[-1][1] >= e:
                continue
            elif merged[-1][1] >= s:
                merged[-1][1] = e
            else:
                merged.append(intervals[i])
        return merged