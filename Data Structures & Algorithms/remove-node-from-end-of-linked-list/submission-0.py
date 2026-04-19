# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: return head

        ptr = head
        count = 1
        while ptr.next:
            count += 1
            ptr = ptr.next
        
        count = count - n
        if count == 0:
            return head.next
        
        ptr = head
        while count > 1:
            ptr = ptr.next
            count -= 1
        ptr.next = ptr.next.next
        return head

