# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        newHead = dummy = ListNode()
        curr = head
        for _ in range(n // k):
            prev = None
            tail = curr
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            dummy.next = prev
            dummy = tail
        
        if curr:
            dummy.next = curr
        
        return newHead.next