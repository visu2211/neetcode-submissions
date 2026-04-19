class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k]
        self.k = k
        heapq.heapify(self.heap)
        for i in range(k, len(nums)):
            if nums[i] > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[i])
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
