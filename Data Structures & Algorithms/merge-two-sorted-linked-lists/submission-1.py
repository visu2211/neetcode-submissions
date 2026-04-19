# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2

        head = curr = ListNode()

        while ptr1 or ptr2:
            if ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    curr.next = ListNode(ptr1.val)
                    curr = curr.next
                    ptr1 = ptr1.next
                else:
                    curr.next = ListNode(ptr2.val)
                    curr = curr.next
                    ptr2 = ptr2.next
            elif ptr1:
                curr.next = ptr1
                break
            else:
                curr.next = ptr2
                break
        return head.next