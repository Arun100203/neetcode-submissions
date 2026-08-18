# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        
        pre = None
        curr = head
        nex = head.next
        

        while curr.next != None:
            curr.next = pre
            pre = curr
            curr = nex
            nex = nex.next

        curr.next = pre
        pre = curr

        return pre
