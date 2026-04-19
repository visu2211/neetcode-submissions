class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freqList = [[] for i in range(len(nums))]
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            freqList[value - 1].append(key)
        result = []
        for index in range(len(freqList) - 1, -1, -1):
            for n in freqList[index]:
                result.append(n)
                if len(result) == k:
                    return result