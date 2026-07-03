class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Read
        Restate
        Inputs / Outputs
            - return starting index where you can travel around and reach back to same spot or -1
        Givens / Assumptions
            - you must collect gas at the first station
                - you start off empty
            - may not be possible
            - at most one solution exists
        Example
            Input: gas = [1,2,3,4], cost = [2,2,4,1]
            Output: 3

            brute force
                try each index and see if you can reach the start
                O(n^2) | O(1)

            you cant do curr += gas[i] - cost[i]
            must deal with cost first and then add gas if curr is not < 0

            sum(gas) must be >= sum(cost) or else is there is insufficient gas to traverse through
        Code
        Edge Cases
        Complexities
        """

        if sum(gas) < sum(cost):
            return -1
        
        #now a valid solution must exist since, in the worse case, there is more than enough gas at one station to compensate for lower stations
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        
        return res