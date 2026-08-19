# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        length = 0

        while fast and fast.next != None:
            fast = fast.next.next
            length += 2

        if fast != None:
            length +=1

        pos = length - n

        cur = head
        i = 1
        if cur.next == None:
            return None
        
        if pos == 0:
            return head.next
        while i != pos:
            i += 1
            cur = cur.next

        if cur.next.next == None:
            cur.next = None
        else:
            cur.next = cur.next.next
        print(cur.val)

        print(length)
        return head
