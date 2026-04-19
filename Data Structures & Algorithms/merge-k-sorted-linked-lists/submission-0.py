# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                if i + 1 == len(lists):
                    mergedList.append(self.merge(lists[i], None))
                else:
                    mergedList.append(self.merge(lists[i], lists[i + 1]))
            lists = mergedList
        
        return lists[0]
                

    def merge(self, l1, l2):
        if not l2:
            return l1
        
        dummy = ListNode()
        ptr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2
        return dummy.next
    