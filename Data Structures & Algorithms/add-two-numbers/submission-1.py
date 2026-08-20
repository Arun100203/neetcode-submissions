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

        while l1 and l2:
            num1 = l1.val
            num2 = l2.val

            total = num1 + num2
            
            add_to_list = total%10

            ans.next = ListNode(add_to_list + carry)
            ans = ans.next

            carry = total//10

            l1 = l1.next
            l2 = l2.next

        while l1:
            num1 = l1.val
            total = num1 + carry
            add_to_list = total%10

            ans.next = ListNode(add_to_list)
            ans = ans.next

            carry = total//10

            l1 = l1.next

        while l2:
            num1 = l2.val
            total = num1 + carry
            add_to_list = total%10

            ans.next = ListNode(add_to_list)
            ans = ans.next

            carry = total//10

            l2 = l2.next

        print(carry)
        if carry != 0:
            ans.next = ListNode(carry)


        return res.next