class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = defaultdict(int)
        for num in nums:
            freqList[num] += 1
        res = []
        for num, count in freqList.items():
            res.append([count, num])
        res.sort()
        fin = []
        while len(fin) < k:
            fin.append(res.pop()[1])
        return fin