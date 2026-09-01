# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        stack = []

        cur = root

        if root == p or root == q:
            return root

        while cur:
            if (p.val <= cur.val <= q.val) or ( q.val <= cur.val <= p.val):
                return cur
            
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left

            elif q.val > cur.val and p.val > cur.val:
                cur = cur.right

            


        return root
            
            

        

            
           