class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #cyclic problem, slow fast
        #slow = nums[i], fast = nums[nums[i]]
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow