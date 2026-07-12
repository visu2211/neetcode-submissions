class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        #if you sort, smallest numbers for 0 and 1 index
        #always choose the smallest interval
        """
        is there ever a case you would choose the larger one

        problem now is the first interval may not always be the smallest interval

        we need to order based off of ascending order and then smallest spanng interval

        if we go based on ascending first then compare between shortest interval,
        prioritizing no smallest could break logic since if the shortest interval
        is the linkage between two interavls, would be better off not including it

        have a heap that 

        when we have an overlapping case, we want to choose the interval that ends first for future intervals
        """
        res = 0
        prevEnd = intervals[0][1]
        for s, e in intervals[1:]:
            if prevEnd <= s:
                prevEnd = e
            else:
                res += 1
                prevEnd = min(e, prevEnd)
        
        return res