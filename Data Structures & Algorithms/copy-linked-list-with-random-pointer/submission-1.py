"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        dic = {}

        curr = head
        while curr:
            dic[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        dummy = ptr = Node(-1, None, None)

        while curr:
            ptr.next = dic[curr]

            if curr.random is None:
                ptr.next.random = None
            else:
                ptr.next.random = dic[curr.random]

            curr = curr.next
            ptr = ptr.next
        
        return dummy.next