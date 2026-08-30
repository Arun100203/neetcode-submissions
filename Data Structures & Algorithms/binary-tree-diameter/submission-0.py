# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def fun(root):
            if not root:
                return 0

            left = right = 0
            if root.left:
                left = 1 + fun(root.left)
            if root.right:
                right = 1 + fun(root.right)
            
            nonlocal ans
            ans = max(ans, left + right)

            # print(left, right, ans, root.val)

            return max(left,right)
        fun(root)

        return ans