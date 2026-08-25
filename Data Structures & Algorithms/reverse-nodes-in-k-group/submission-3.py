# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = head

        ans = ListNode(-1)
        res = ans
        while temp:
            temp_head = temp
            n = 1
            while n < k and temp.next:
                temp = temp.next
                n += 1
            if n < k or temp == None:
                break
            
            pre_temp = temp
            temp = temp.next if temp else None

            pre_temp.next = None if pre_temp else None
            cur_head, cur_tail = self.reverse(temp_head)

            ans.next = cur_head
            ans = cur_tail

        if n < k and temp != None:
            ans.next = temp_head

        return res.next

            

    def reverse(self, head):
        pre = None
        cur = head
        end = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre, end

                