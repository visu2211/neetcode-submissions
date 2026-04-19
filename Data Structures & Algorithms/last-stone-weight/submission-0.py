class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            fS, sS = heapq.heappop(heap), heapq.heappop(heap)

            if fS == sS:
                continue
            newStone = (fS * -1) - (sS * -1)
            heapq.heappush(heap, -newStone)
        
        return 0 if heap == [] else -heap[0]