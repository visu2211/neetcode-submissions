class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        counter = Counter(hand)
        hand.sort()

        for num in hand:
            if counter[num] == 0:
                continue
            for j in range(num, num + groupSize):
                if j not in counter or counter[j] == 0:
                    return False
                counter[j] -= 1
        return True
        """

        1 2 3 3 4 4 5 6 

        1: 1
        2: 1
        3: 2
        4: 2
        5: 1
        6: 1


        Strategy 1:
            sort the cards in order
            starting from the beginning try to get numbers in a row, track their indices in a visited set
            if values are the same as previous skip them
            by the end, if the length of the set is the same as hand then it is possible
            while:
                for:
            Brute Force: O((n / groupsize) * n)

        Strategy 2:
            Keep a hashmap counting frequencies.
            start from the beginning of the hashmap still have to repeat n / groupsize * n times

        Point is to avoid doing multiple passes
        
        Strategy 3:
            list of lists
            for each number thats the same distribute it, if different keep going until you're done
            then go next one
        """