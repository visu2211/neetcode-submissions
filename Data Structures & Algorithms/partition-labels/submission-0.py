class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        want to split the string into as amny substrings as possible
            each substring cannot overlap in letters

        have a hashmap that records the first and last index of the letter
        b: 6, 9
        x: 0, 3
        y: 1, 4
        z: 5, 7
        i: 10, 10
        s: 11, 11
        l = 12, 12

        how do you figure out which ones to combine
            if they overlap in interval you must combine
                you cant split up any interval
        """
        hMap = {}
        for i, l in enumerate(s):
            if l not in hMap:
                hMap[l] = [i, i]
            else:
                hMap[l][1] = i
        
        bounds = []
        for l in hMap:
            bounds.append(hMap[l])
        bounds.sort()
        res = []
        merged = [bounds[0]]
        
        for i in range(1, len(bounds)):
            s, e = bounds[i]
            if merged[-1][1] > e:
                continue
            elif merged[-1][1] > s:
                merged[-1][1] = e
            else:
                res.append(merged[-1][1] - merged[-1][0] + 1)
                merged.append(bounds[i])
        res.append(merged[-1][1] - merged[-1][0] + 1)
        return res
