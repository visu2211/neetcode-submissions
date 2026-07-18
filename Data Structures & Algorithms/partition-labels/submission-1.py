class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        want to split the string into as many substrings as possible
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
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        size = 0
        substringEnd = 0
        res = []
        for i, c in enumerate(s):
            size += 1
            substringEnd = max(substringEnd, lastIndex[c])

            if i == substringEnd:
                res.append(size)
                size = 0
                substringEnd = 0
        return res