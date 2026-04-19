class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i, v in enumerate(nums):

            if q and i - q[0] == k:
                q.popleft()
            
            while q and v > nums[q[-1]]:
                q.pop()
            
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res