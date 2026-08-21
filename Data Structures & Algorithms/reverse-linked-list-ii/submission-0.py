# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        
        

        leftPre = None
        leftPreHead = head
        leftPoin = head
        leftCache = left
        while left - 1 != 0:
            leftPre = leftPoin
            leftPoin = leftPoin.next
        
            left -= 1
        
        if leftPre:
            leftPre.next = None
        
        

        right = right - leftCache + 1

        start = leftPoin

        while right - 1 != 0:
            leftPoin = leftPoin.next

            right -= 1

        remainingRight = leftPoin.next
        leftPoin.next = None

        pre = None
        cur = start

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # while pre:
        #     print(pre.val)
        #     pre = pre.next

        
        if leftPre:
            leftPre.next = pre

        start.next = remainingRight
        # print(remainingRight.val)

        return head if leftCache > 1 else pre
        


        