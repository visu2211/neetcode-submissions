# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, ptr, post = None, head, None
        if not head:
            return None
        
        while ptr:
            post = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = post
        
        return prev