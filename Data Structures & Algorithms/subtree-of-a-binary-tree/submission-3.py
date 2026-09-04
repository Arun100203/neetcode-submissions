# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = []

        stack.append(root)

        def isSame(root, sub):
            if not root and not sub:
                return True

            if not root and sub:
                return False
            
            if root and not sub:
                return False 
                
            if root.val != sub.val:
                return False



            return isSame(root.left, sub.left) and isSame(root.right, sub.right)

        ans = False

        while stack:

            last = stack.pop()
            # print(last.val, stack)
            if last.val == subRoot.val:
                ans = ans or isSame(last, subRoot)

            if last.left:
                stack.append(last.left)
            if last.right:
                stack.append(last.right)

        return ans

        
        
        