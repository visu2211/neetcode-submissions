# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False

        fast, slow = head.next.next, head.next

        while fast.next and fast.next.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False