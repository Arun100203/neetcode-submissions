# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        ans = True

        def dep(root):
            if not root:
                return 0

            left = 1 + dep(root.left)
            right = 1 + dep(root.right)

            if left - right > 1 or right - left > 1:
                nonlocal ans
                ans = False

            return max(left, right)

        dep(root)

        return ans