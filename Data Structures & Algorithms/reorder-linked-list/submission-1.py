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
        cur = slow
        aft = slow.next
        

        while cur.next != None:
            cur.next = pre
            pre = cur
            cur = aft
            aft = aft.next

        cur.next = pre
        pre = cur

        start = head
        # while pre:
        #     print(pre.val)
        #     pre = pre.next

        # print("=======")

        # while start:
        #     print(start.val)
        #     start = start.next
            
        ans = ListNode(-1)
        res = ans
        while pre and start.next != None:
            ans.next = start
            start = start.next
            ans = ans.next
            ans.next = pre
            pre = pre.next
            ans = ans.next


        # while res != None:
        #     print(res.val)
        #     res = res.next
        