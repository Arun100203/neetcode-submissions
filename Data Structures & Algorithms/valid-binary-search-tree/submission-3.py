# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def fun(root, low, maxi):
            if not root:
                return True

            left, right = root.left, root.right

            if not (low < root.val < maxi):
                return False

            return fun(left, low, root.val) and fun(right, root.val, maxi)

        return fun(root, float('-inf'), float('inf'))

        