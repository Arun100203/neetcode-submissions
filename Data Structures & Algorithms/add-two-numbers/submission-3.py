# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (l1 and l1.val == 0) or (l2 and l2.val == 0):
            return l2 if l1.val == 0 else l1

        ans = ListNode(-1)
        res = ans
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            total = num1 + num2 + carry
            ans.next = ListNode(total%10)
            carry = total // 10

            ans = ans.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next