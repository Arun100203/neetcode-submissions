# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        pre = None
        cur = slow.next
        
        slow.next = None
        while cur != None:
            aft = cur.next
            cur.next = pre
            pre = cur
            cur = aft

       
        start = head
        # while pre:
        #     print(pre.val)
        #     pre = pre.next

        # print("=======")

        # while start:
        #     print(start.val)
        #     start = start.next
            
        first = start
        second = pre
        while first and second:
            
            first_next = first.next
            sec_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = sec_next


        # while res != None:
        #     print(res.val)
        #     res = res.next
        