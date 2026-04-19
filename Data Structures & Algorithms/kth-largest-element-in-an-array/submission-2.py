class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            if heap[0] < nums[i]:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
        return heap[0]