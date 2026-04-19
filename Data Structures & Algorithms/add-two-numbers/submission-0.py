# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return []
        
        ptr, i, num1 = l1, 1, 0
        while ptr:
            num1 += ptr.val * i
            i *= 10
            ptr = ptr.next
        
        ptr, i, num2 = l2, 1, 0
        while ptr:
            num2 += ptr.val * i
            i *= 10
            ptr = ptr.next
        
        s = num1 + num2
        head = ListNode(s % 10)
        ptr = head
        s //= 10
        while s > 0:
            ptr.next = ListNode(s % 10)
            s //= 10
            ptr = ptr.next
        return head