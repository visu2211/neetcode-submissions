class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hMap = {}
        for n in nums:
            if n in hMap:
                hMap[n] += 1
            else:
                hMap[n] = 1
        
        for v, f in hMap.items():
            heapq.heappush(heap, (-f, v))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res