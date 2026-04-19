class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i, curr in enumerate(nums):
            #popping indices if nums[index] is less than curr, keeps the max at the beginning of the queue
            if q and i - q[0] == k:
                q.popleft()
            
            while q and nums[q[-1]] <= curr:
                q.pop()
            #add element to queue
            q.append(i)

            #shrinking window if window is of size k + 1
            
            #adding value to res if window is of size k
            if i >= k - 1:
                res.append(nums[q[0]])
            print(q)
        return res

        # 7 2 4
