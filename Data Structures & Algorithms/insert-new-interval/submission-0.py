class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if merged[-1][1] >= s and merged[-1][1] >= e:
                continue
            elif merged[-1][1] >= s:
                merged[-1][1] = e
            else:
                merged.append(intervals[i])
        
        return merged