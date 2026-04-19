# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        ptr, ptr2 = head, head
        while ptr.next and ptr2:
            ptr = ptr.next
            ptr2 = ptr2.next.next
            if ptr2 == ptr:
                return True
        return False