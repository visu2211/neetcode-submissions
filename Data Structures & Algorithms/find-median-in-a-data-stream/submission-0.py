class MedianFinder:

    def __init__(self):
        #self.left holds bottom 50 percentile values (invert values so you get largest)
        #self.right holds top 50 percentile values
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        #add num into correct list
        #right by default, we add to left if it is less than current highest value
        #not doing so would only add values into the left when reshuffling
        if self.left and -self.left[0] > num:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        #if not balanced rebalance
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                val = -heapq.heappop(self.left)
                heapq.heappush(self.right, val)
            else:
                val = heapq.heappop(self.right)
                heapq.heappush(self.left, -val)
        

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        else:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]
