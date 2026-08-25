# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        de = deque(lists)
        
        while len(de) != 1:
            l1 = de.popleft() if len(de) >= 1 else None
            l2 = de.popleft() if len(de) >= 1 else None
            de.append(self.mergeList(l1, l2))


        return de[-1]

    def mergeList(self, head1, head2):

        res = ListNode(-1)
        ans = res

        while head1 and head2:
            if head1.val < head2.val:
                res.next = head1
                head1 = head1.next
            else:
                res.next = head2
                head2 = head2.next

            res = res.next

        if head1 != None:
            res.next = head1
        if head2 != None:
            res.next = head2

        return ans.next
            
            
        