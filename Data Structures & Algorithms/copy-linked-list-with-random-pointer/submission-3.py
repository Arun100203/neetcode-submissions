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
        if head == None:
            return None
        
        res = Node(-1)
        temp = res
        d1 = {}
        head1 = head
        while head != None:
            temp_head = Node(head.val)
            
            if head not in d1:
                d1[head] = temp_head
            else:
                d1[head].append(temp_head)

            head = head.next

        ans = None
        if head1.next == None:
            te = d1[head1] 
            

            if head1.random != None:
                random_node = d1[head1.random]
            else:
                random_node = None

            te.random = random_node

            return te

        while head1.next != None:
            new_node = d1[head1]

            if ans == None:
                ans = new_node
            
            next_node = d1[head1.next]
            if head1.random != None:
                random_node = d1[head1.random]
            else:
                random_node = None
            # print(head1.val, head1.next.val, random_node and random_node.val)
            
            
            new_node.next = next_node
            new_node.random = random_node 
            # print(new_node.val, new_node.next.val)

            head1 = head1.next


        # print(head1.val)
        new_node = d1[head1]
        next_node = None
        if head1.random != None:
            random_node = d1[head1.random]
        else:
            random_node = None

        new_node.next = next_node
        new_node.random = random_node



        return ans
