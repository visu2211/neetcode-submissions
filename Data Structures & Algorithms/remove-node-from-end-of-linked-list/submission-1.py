# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head

        if n == 0 or not head.next:
            return head.next

        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        exit = count - n - 1
        curr = head

        if exit == -1:
            return head.next
        
        for _ in range(exit):
            curr = curr.next

        curr.next = curr.next.next
        return head



        
        