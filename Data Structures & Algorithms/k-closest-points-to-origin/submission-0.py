class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            val = p[0] ** 2 + p[1] ** 2
            if len(heap) < k or -heap[0][0] > val:
                heapq.heappush(heap, (-val, p))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [p for val, p in heap]